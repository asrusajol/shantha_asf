from bs4 import BeautifulSoup
from utils.http import session
from config.settings import DASHBOARD_URL

def scrape_dashboard():
    r = session.get(DASHBOARD_URL)
    soup = BeautifulSoup(r.text, "lxml")

    table = soup.find("table", class_="dashboard-table")
    headers = [th.text.strip() for th in table.find("thead").find_all("th")]

    data = []
    for tr in table.find("tbody").find_all("tr"):
        row = []
        for td in tr.find_all("td"):
            link = td.find("a")
            row.append(link["href"] if link else td.text.strip())
        data.append(dict(zip(headers, row)))
    return data