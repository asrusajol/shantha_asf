import requests
from bs4 import BeautifulSoup
from dateutil import parser
from config import NAV_URL, FUND_NAME


def clean_decimal(value):
    return float(value.replace("\xa0", "").strip())


def parse_date(value):
    return parser.parse(value).date()


def scrape_nav_data():
    response = requests.get(NAV_URL, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # 🔍 Step 1: Find the correct section by heading text
    heading = soup.find("h4", string=lambda x: x and "Buy and Sale Rate" in x)

    if not heading:
        raise RuntimeError("Buy and Sale Rate section not found")

    # 🔍 Step 2: Locate the container div
    container = heading.find_parent("div", class_="col-sm-12")

    if not container:
        raise RuntimeError("NAV container div not found")

    # 🔍 Step 3: Find the table inside this section only
    table = container.find("table")

    if not table:
        raise RuntimeError("NAV table not found inside Buy and Sale Rate section")

    records = []

    tbody = table.find("tbody")
    rows = tbody.find_all("tr")

    for row in rows:
        cols = [c.get_text(strip=True) for c in row.find_all("td")]

        record = (
            FUND_NAME,
            parse_date(cols[0]),     # NAV Date
            clean_decimal(cols[1]),  # NAV at Market Price
            clean_decimal(cols[2]),  # Unit Buy Price
            clean_decimal(cols[3]),  # Redemption Price
            parse_date(cols[4]),     # Effective Date
        )

        records.append(record)

    return records
