from auth.login import login
from scrapers.nav_scraper import scrape_nav
from scrapers.dashboard_scraper import scrape_dashboard
from storage.nav_repository import save_nav
from storage.dashboard_repository import save_snapshot
from config.settings import PORTAL_USERNAME, PORTAL_PASSWORD


for nav in scrape_nav():
    save_nav(nav)

login(PORTAL_USERNAME,PORTAL_PASSWORD)
for row in scrape_dashboard():
    save_snapshot(row)

print(f"✅ NAV & Dashboard data successfully stored")