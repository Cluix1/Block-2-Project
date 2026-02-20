import html
from pathlib import Path

from django.http import HttpResponse

USERS = [
    {"username": "admin", "password": "s3cret"},
    {"username": "alice", "password": "password1"},
]


def simulate_sql_injection_login(username: str, password: str) -> bool:
    injection_patterns = [
        "or '1'=='1'", 'or "1"=="1"', "or 1=1", "or 'a'='a" , 'or "a"="a"', "' or '1'='1", '" or "1"="1']
    uname = username.lower().replace(' ', '')
    pword = password.lower().replace(' ', '')
    if any(pattern in uname or pattern in pword for pattern in injection_patterns):
        return True
    return any(
        user["username"] == username and user["password"] == password
        for user in USERS
    )


def evaluate_clause(clause: str, user: dict) -> bool:



def simulate_safe_login(username: str, password: str) -> bool:
    return any(
        user["username"] == username and user["password"] == password
        for user in USERS
    )


def sql_injection_demo_view(request):
    result = ""
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if simulate_safe_login(username, password):
            result = "Regular login succeeded."
        elif simulate_sql_injection_login(username, password):
            result = "Injection succeeded (bypassed login)."
        else:
            result = "Login failed."

    # Read the HTML file and do a simple string replacement for the result
    template_path = Path(__file__).resolve().parent.parent / "templates" / "index.html"
    html_content = template_path.read_text(encoding="utf-8")
    if result:
        html_content = html_content.replace(
            "Result will appear here after login", result, 1
        ).replace("result-box placeholder", "result-box", 1)
    return HttpResponse(html_content)
