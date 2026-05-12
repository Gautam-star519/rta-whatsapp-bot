import sqlite3
DB = "data.db"
def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dividend_status(company TEXT, status TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS mgt7_status(company TEXT, status TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS drn_codes(code TEXT, meaning TEXT)")
    cur.execute("DELETE FROM dividend_status")
    cur.execute("DELETE FROM mgt7_status")
    cur.execute("DELETE FROM drn_codes")
    cur.execute("INSERT INTO dividend_status VALUES ('coal india', 'Unpaid Dividend as on 31.03.2026 uploaded successfully.')")
    cur.execute("INSERT INTO mgt7_status VALUES ('nahar capital', 'MGT-7 file generated and available on shared path.')")
    cur.execute("INSERT INTO drn_codes VALUES ('51', 'Processed and awaiting confirmation.')")
    conn.commit(); conn.close()

def lookup(table, key_col, value_col, key):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(f"SELECT {value_col} FROM {table} WHERE lower({key_col}) = lower(?)", (key,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None