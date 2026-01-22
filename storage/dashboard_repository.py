from config.database import cursor
from utils.helpers import clean_number
from datetime import date

def save_snapshot(row):
    sql = """
    INSERT INTO investment_snapshots
    (fund_name, account_type, investment_type, units_held,
    investment_cost, market_value, dividend_income,
    dividend_receivable, total_return, details_url, snapshot_date)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    try:
        cursor.execute(sql, (
            row["Fund Name"],
            row["Account Type"],
            row["Investment Type"],
            clean_number(row["Units Held"]),
            clean_number(row["Investment at Cost"]),
            clean_number(row["Market Value of Investment"]),
            clean_number(row["Dividend Income"]),
            clean_number(row["Dividend Receivable"]),
            clean_number(row["Total Return"]),
            row["Particulars"],
            date.today()
        ))
    except Exception as e:
        print(e)