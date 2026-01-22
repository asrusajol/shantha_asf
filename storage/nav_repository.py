from config.database import cursor

def save_nav(nav):

    sql = """
    INSERT INTO nav_history
    (fund_name, nav_date, nav_market, buy_price, redemption_price, effective_date)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    try:
        cursor.execute(sql, nav)
    except Exception as e:
        print(e)

