from bs4 import BeautifulSoup
from utils.http import session
from config.settings import LOGIN_URL, DASHBOARD_URL


def login(username, password):
    # --------------------------------------------------
    # Step 1: Load login page (get CSRF token)
    # --------------------------------------------------
    resp = session.get(LOGIN_URL)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    csrf = soup.find("input", {"name": "_token"})["value"]

    # --------------------------------------------------
    # Step 2: Submit login form
    # --------------------------------------------------
    payload = {
        "_token": csrf,
        "username": username,
        "password": password,
    }

    login_resp = session.post(
        LOGIN_URL,
        data=payload,
        headers={"Referer": LOGIN_URL},
        allow_redirects=True,
    )
    login_resp.raise_for_status()

    if "auth/login" in login_resp.url:
        raise Exception("Login failed")

    print("✅ Login successful")

    return True
