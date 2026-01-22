import os

# Web URL
NAV_URL = "https://shanta-aml.com/our-funds/shanta-amanah-shariah-fund"

# Fund Info
FUND_NAME = "Shanta Amanah Shariah Fund"

# MySQL DB connection

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "user_name"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "database": os.getenv("DB_NAME", "database_name"),
}

# Logging

LOG_FILE = "logs/nav_scraper.log"