import mysql.connector
from config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def insert_nav_records(records):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO nav_history
    (fund_name, nav_date, nav_market_price, unit_buy_price, redemption_price, effective_date)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        nav_market_price = VALUES(nav_market_price),
        unit_buy_price = VALUES(unit_buy_price),
        redemption_price = VALUES(redemption_price),
        effective_date = VALUES(effective_date)
    """

    cursor.executemany(sql, records)
    conn.commit()

    cursor.close()
    conn.close()