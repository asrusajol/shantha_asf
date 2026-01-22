import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://webportal.shanta-aml.com"
LOGIN_URL = f"{BASE_URL}/auth/login"
DASHBOARD_URL = f"{BASE_URL}/investor/dashboard"
NAV_URL = "https://shanta-aml.com/our-funds/shanta-amanah-shariah-fund"
FUND_NAME = "Shanta Amanah Shariah Fund"

PORTAL_USERNAME = os.getenv("PORTAL_USERNAME")
PORTAL_PASSWORD = os.getenv("PORTAL_PASSWORD")