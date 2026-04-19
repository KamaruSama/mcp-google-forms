"""
================================================================================
 Google Forms MCP Server
================================================================================

 A Model Context Protocol server exposing 19 tools to create, edit, inspect,
 and manage Google Forms — including quiz grading, image attachments, and
 response management.

 Transport : stdio
 Auth      : OAuth 2.0 (Desktop flow). Credentials at ~/.config/google-forms-mcp/
 Scopes    : forms.body, forms.responses.readonly, drive.file

--------------------------------------------------------------------------------
 Copyright © 2026 likezara™. All rights reserved.
 Developed by Kamaru (pen name).
--------------------------------------------------------------------------------
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Literal

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP

# ─────────────────────────────────────────────────────────────────────────────
#  Configuration
# ─────────────────────────────────────────────────────────────────────────────

SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/forms.responses.readonly",
    "https://www.googleapis.com/auth/drive.file",
]

CONFIG_DIR = Path(
    os.environ.get("GOOGLE_FORMS_MCP_DIR", Path.home() / ".config/google-forms-mcp")
)
CREDENTIALS_PATH = CONFIG_DIR / "credentials.json"
TOKEN_PATH = CONFIG_DIR / "token.json"

mcp = FastMCP("google-forms")


# ─────────────────────────────────────────────────────────────────────────────
#  Auth + internal helpers
# ─────────────────────────────────────────────────────────────────────────────

def _get_service():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    creds: Credentials | None = None

    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_PATH.exists():
                raise FileNotFoundError(
                    f"Place OAuth desktop credentials at {CREDENTIALS_PATH}. "
                    "See https://developers.google.com/forms/api/quickstart/python"
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_PATH), SCOPES
            )
            creds = flow.run_local_server(port=0)
        TOKEN_PATH.write_text(creds.to_json())

    return build("forms", "v1", credentials=creds, cache_discovery=False)


def _batch_update(form_id: str, requests: list[dict[str, Any]]) -> dict[str, Any]:
    return (
        _get_service()
        .forms()
        .batchUpdate(formId=form_id, body={"requests": requests})
        .execute()
    )


def _tf_item(
    title: str, correct: bool, points: int = 1, required: bool = True
) -> dict[str, Any]:
    """Build a True/False question (RADIO with 2 options) including answer key."""
    return {
        "title": title,
        "questionItem": {
            "question": {
                "required": required,
                "grading": {
                    "pointValue": points,
                    "correctAnswers": {
                        "answers": [{"value": "ถูก" if correct else "ผิด"}]
                    },
                },
                "choiceQuestion": {
                    "type": "RADIO",
                    "options": [{"value": "ถูก"}, {"value": "ผิด"}],
                    "shuffle": False,
                },
            }
        },
    }


# ═════════════════════════════════════════════════════════════════════════════
#  Section 1 · Auth & diagnostics
# ═════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def auth_status() -> dict[str, Any]:
    """Report whether OAuth credentials and token are in place."""
    return {
        "config_dir": str(CONFIG_DIR),
        "credentials_present": CREDENTIALS_PATH.exists(),
        "token_present": TOKEN_PATH.exists(),
        "credentials_path": str(CREDENTIALS_PATH),
    }


# ═════════════════════════════════════════════════════════════════════════════
#  Section 2 · Form creation & metadata
# ═════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def create_quiz_form(
    title: str, document_title: str | None = None
) -> dict[str, Any]:
    """Create a new Google Form in quiz mode. Returns formId and responderUri."""
    svc = _get_service()
    form = (
        svc.forms()
        .create(body={"info": {"title": title, "documentTitle": document_title or title}})
        .execute()
    )
    form_id = form["formId"]
    _batch_update(
        form_id,
        [
            {
                "updateSettings": {
                    "settings": {"quizSettings": {"isQuiz": True}},
                    "updateMask": "quizSettings.isQuiz",
                }
            }
        ],
    )
    return {
        "formId": form_id,
        "responderUri": form.get("responderUri"),
        "editUrl": f"https://docs.google.com/forms/d/{form_id}/edit",
    }


@mcp.tool()
def rename_form(
    form_id: str,
    title: str | None = None,
    description: str | None = None,
    document_title: str | None = None,
) -> dict[str, Any]:
    """Update form's displayed title, description, and/or Drive document title."""
    info: dict[str, Any] = {}
    masks: list[str] = []
    if title is not None:
        info["title"] = title
        masks.append("title")
    if description is not None:
        info["description"] = description
        masks.append("description")
    if document_title is not None:
        info["documentTitle"] = document_title
        masks.append("documentTitle")
    if not masks:
        raise ValueError("provide at least one of title/description/document_title")
    return _batch_update(
        form_id,
        [{"updateFormInfo": {"info": info, "updateMask": ",".join(masks)}}],
    )


@mcp.tool()
def set_quiz_mode(form_id: str, is_quiz: bool = True) -> dict[str, Any]:
    """Toggle quiz grading mode on/off."""
    return _batch_update(
        form_id,
        [
            {
                "updateSettings": {
                    "settings": {"quizSettings": {"isQuiz": is_quiz}},
                    "updateMask": "quizSettings.isQuiz",
                }
            }
        ],
    )


# ═════════════════════════════════════════════════════════════════════════════
#  Section 3 · Read & inspect
# ═════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def get_form(form_id: str) -> dict[str, Any]:
    """Fetch full form metadata, items, and settings."""
    return _get_service().forms().get(formId=form_id).execute()


@mcp.tool()
def list_questions(form_id: str) -> list[dict[str, Any]]:
    """Return a concise list of items: index, itemId, title, correctAnswer, points."""
    form = _get_service().forms().get(formId=form_id).execute()
    out = []
    for i, item in enumerate(form.get("items", [])):
        q = item.get("questionItem", {}).get("question", {})
        grading = q.get("grading", {})
        answers = grading.get("correctAnswers", {}).get("answers", [])
        out.append(
            {
                "index": i,
                "itemId": item.get("itemId"),
                "title": item.get("title"),
                "correctAnswer": [a.get("value") for a in answers] or None,
                "points": grading.get("pointValue"),
            }
        )
    return out


@mcp.tool()
def verify_answer_keys(
    form_id: str, expected: list[dict[str, Any]]
) -> dict[str, Any]:
    """Compare current answer keys to an expected list.

    Each expected item: {"index": int, "correct": "ถูก"|"ผิด"|str}.
    Returns {matches: [...], mismatches: [...]}.
    """
    form = _get_service().forms().get(formId=form_id).execute()
    items = form.get("items", [])
    matches, mismatches = [], []
    for exp in expected:
        idx = exp["index"]
        want = exp["correct"]
        if idx >= len(items):
            mismatches.append({"index": idx, "error": "out of range"})
            continue
        q = items[idx].get("questionItem", {}).get("question", {})
        actual = [
            a.get("value")
            for a in q.get("grading", {}).get("correctAnswers", {}).get("answers", [])
        ]
        entry = {
            "index": idx,
            "title": items[idx].get("title"),
            "expected": want,
            "actual": actual,
        }
        if actual == [want] or want in actual:
            matches.append(entry)
        else:
            mismatches.append(entry)
    return {"matches": matches, "mismatches": mismatches}


# ═════════════════════════════════════════════════════════════════════════════
#  Section 4 · Add questions
# ═════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def add_true_false_question(
    form_id: str,
    title: str,
    correct_answer: bool,
    points: int = 1,
    index: int | None = None,
    required: bool = True,
) -> dict[str, Any]:
    """Append (or insert at index) a True/False question with answer key."""
    form = _get_service().forms().get(formId=form_id).execute()
    loc = index if index is not None else len(form.get("items", []))
    return _batch_update(
        form_id,
        [
            {
                "createItem": {
                    "item": _tf_item(title, correct_answer, points, required),
                    "location": {"index": loc},
                }
            }
        ],
    )


@mcp.tool()
def batch_add_true_false(
    form_id: str,
    questions: list[dict[str, Any]],
    start_index: int | None = None,
    clear_existing: bool = False,
) -> dict[str, Any]:
    """Bulk add True/False questions.

    Each question dict: {"title": str, "correct": bool, "points": int?, "required": bool?}.
    If clear_existing=True, deletes all existing items first.
    """
    svc = _get_service()
    form = svc.forms().get(formId=form_id).execute()
    existing = form.get("items", [])

    requests: list[dict[str, Any]] = []
    if clear_existing and existing:
        for i in range(len(existing) - 1, -1, -1):
            requests.append({"deleteItem": {"location": {"index": i}}})
        base = 0
    else:
        base = start_index if start_index is not None else len(existing)

    for offset, q in enumerate(questions):
        requests.append(
            {
                "createItem": {
                    "item": _tf_item(
                        title=q["title"],
                        correct=bool(q["correct"]),
                        points=int(q.get("points", 1)),
                        required=bool(q.get("required", True)),
                    ),
                    "location": {"index": base + offset},
                }
            }
        )
    return _batch_update(form_id, requests)


@mcp.tool()
def add_multiple_choice_question(
    form_id: str,
    title: str,
    options: list[str],
    correct_answers: list[str],
    points: int = 1,
    kind: Literal["RADIO", "CHECKBOX", "DROP_DOWN"] = "RADIO",
    index: int | None = None,
    required: bool = True,
) -> dict[str, Any]:
    """Add a choice question (radio/checkbox/dropdown) with answer key."""
    form = _get_service().forms().get(formId=form_id).execute()
    loc = index if index is not None else len(form.get("items", []))
    item = {
        "title": title,
        "questionItem": {
            "question": {
                "required": required,
                "grading": {
                    "pointValue": points,
                    "correctAnswers": {
                        "answers": [{"value": v} for v in correct_answers]
                    },
                },
                "choiceQuestion": {
                    "type": kind,
                    "options": [{"value": v} for v in options],
                    "shuffle": False,
                },
            }
        },
    }
    return _batch_update(
        form_id, [{"createItem": {"item": item, "location": {"index": loc}}}]
    )


@mcp.tool()
def add_text_question(
    form_id: str,
    title: str,
    correct_answers: list[str] | None = None,
    points: int = 0,
    paragraph: bool = False,
    index: int | None = None,
    required: bool = True,
) -> dict[str, Any]:
    """Add a short-answer or paragraph text question. Optional answer key."""
    form = _get_service().forms().get(formId=form_id).execute()
    loc = index if index is not None else len(form.get("items", []))
    question: dict[str, Any] = {
        "required": required,
        "textQuestion": {"paragraph": paragraph},
    }
    if correct_answers:
        question["grading"] = {
            "pointValue": points,
            "correctAnswers": {
                "answers": [{"value": v} for v in correct_answers]
            },
        }
    return _batch_update(
        form_id,
        [
            {
                "createItem": {
                    "item": {"title": title, "questionItem": {"question": question}},
                    "location": {"index": loc},
                }
            }
        ],
    )


@mcp.tool()
def add_section_header(
    form_id: str,
    title: str,
    description: str | None = None,
    index: int | None = None,
) -> dict[str, Any]:
    """Add a page-break / section header."""
    form = _get_service().forms().get(formId=form_id).execute()
    loc = index if index is not None else len(form.get("items", []))
    item: dict[str, Any] = {"title": title, "pageBreakItem": {}}
    if description:
        item["description"] = description
    return _batch_update(
        form_id, [{"createItem": {"item": item, "location": {"index": loc}}}]
    )


# ═════════════════════════════════════════════════════════════════════════════
#  Section 5 · Edit & manage questions
# ═════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def update_question_title(
    form_id: str, index: int, new_title: str
) -> dict[str, Any]:
    """Change the title/text of the question at the given index."""
    return _batch_update(
        form_id,
        [
            {
                "updateItem": {
                    "item": {"title": new_title},
                    "location": {"index": index},
                    "updateMask": "title",
                }
            }
        ],
    )


@mcp.tool()
def update_true_false_answer(
    form_id: str, index: int, correct_answer: bool, points: int = 1
) -> dict[str, Any]:
    """Update the answer key (correct T/F) for a True/False question at index."""
    form = _get_service().forms().get(formId=form_id).execute()
    items = form.get("items", [])
    if index >= len(items):
        raise IndexError(f"index {index} out of range ({len(items)} items)")
    current = items[index]
    new_item = _tf_item(
        title=current.get("title", ""),
        correct=correct_answer,
        points=points,
        required=current.get("questionItem", {})
        .get("question", {})
        .get("required", True),
    )
    return _batch_update(
        form_id,
        [
            {
                "updateItem": {
                    "item": new_item,
                    "location": {"index": index},
                    "updateMask": "questionItem.question",
                }
            }
        ],
    )


@mcp.tool()
def delete_question(form_id: str, index: int) -> dict[str, Any]:
    """Delete the item at the given index."""
    return _batch_update(
        form_id, [{"deleteItem": {"location": {"index": index}}}]
    )


@mcp.tool()
def move_question(
    form_id: str, from_index: int, to_index: int
) -> dict[str, Any]:
    """Reorder a question from one index to another."""
    return _batch_update(
        form_id,
        [
            {
                "moveItem": {
                    "originalLocation": {"index": from_index},
                    "newLocation": {"index": to_index},
                }
            }
        ],
    )


# ═════════════════════════════════════════════════════════════════════════════
#  Section 6 · Responses
# ═════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def list_responses(form_id: str) -> dict[str, Any]:
    """List submitted responses for a form."""
    return _get_service().forms().responses().list(formId=form_id).execute()


@mcp.tool()
def get_response(form_id: str, response_id: str) -> dict[str, Any]:
    """Fetch a single response by id."""
    return (
        _get_service()
        .forms()
        .responses()
        .get(formId=form_id, responseId=response_id)
        .execute()
    )


# ═════════════════════════════════════════════════════════════════════════════
#  Section 7 · Escape hatch
# ═════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def raw_batch_update(
    form_id: str, requests: list[dict[str, Any]]
) -> dict[str, Any]:
    """Escape hatch: pass raw Google Forms API batchUpdate requests."""
    return _batch_update(form_id, requests)


# ─────────────────────────────────────────────────────────────────────────────
#  Entrypoint
# ─────────────────────────────────────────────────────────────────────────────

def main():
    """Entry point for  console script."""
    mcp.run()


if __name__ == "__main__":
    main()
