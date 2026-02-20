import html
from pathlib import Path

from django.http import HttpResponse

USERS = [
    {"username": "admin", "password": "s3cret"},
    {"username": "alice", "password": "password1"},
]


def vulnerable_login(username: str, password: str) -> bool:
    query = "username = '{}' AND password = '{}'".format(username, password)
    for user in USERS:
        if evaluate_query(query, user):
            return True
    return False


def evaluate_query(query: str, user: dict) -> bool:
    parts = [p.strip() for p in query.split("AND")]
    return all(evaluate_clause(part, user) for part in parts)


def evaluate_clause(clause: str, user: dict) -> bool:
    if "OR" in clause:
        return True
    if "=" not in clause:
        return False
    left, right = [p.strip() for p in clause.split("=", 1)]
    right = right.strip("'")
    return user.get(left) == right


def safe_login(username: str, password: str) -> bool:
    return any(
        user["username"] == username and user["password"] == password
        for user in USERS
    )


def index(request):
    result = ""

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        regular_ok = safe_login(username, password)
        vuln_ok = vulnerable_login(username, password)

        if regular_ok:
            result = "Regular login succeeded."
        elif vuln_ok:
            result = "Injection succeeded (bypassed login)."
        else:
            result = "Login failed."

    safe_result = html.escape(result) if result else "Result will appear here after login"

    template_path = Path(__file__).resolve().parent.parent / "templates" / "index.html"
    template = template_path.read_text(encoding="utf-8")

    if result:
        html_content = template.replace(
            "Result will appear here after login", safe_result, 1
        ).replace("result-box placeholder", "result-box", 1)
    else:
        html_content = template

    return HttpResponse(html_content)
