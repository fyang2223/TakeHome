
def create_lang_table(con, lang_table, ctry_table):
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {lang_table}(
        country_code TEXT NOT NULL,
        code TEXT NOT NULL,
        name TEXT,
        native TEXT,
        rtl INTEGER NOT NULL,
        FOREIGN KEY(country_code) REFERENCES {ctry_table}(country_code)
    )
    """
    cur = con.cursor()
    cur.execute(create_table_query)


def create_cont_table(con, cont_table, ctry_table):
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {cont_table}(
        country_code TEXT NOT NULL,
        code TEXT NOT NULL,
        name TEXT NOT NULL,
        FOREIGN KEY(country_code) REFERENCES {ctry_table}(country_code)
    )
    """
    cur = con.cursor()
    cur.execute(create_table_query)


def create_curr_table(con, curr_table, ctry_table):
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {curr_table}(
        country_code TEXT NOT NULL,
        currency TEXT,
        FOREIGN KEY(country_code) REFERENCES {ctry_table}(country_code)
    )
    """
    cur = con.cursor()
    cur.execute(create_table_query)

def create_ctry_table(con, ctry_table):
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {ctry_table}(
        code TEXT NOT NULL PRIMARY KEY,
        name TEXT NOT NULL,
        native TEXT NOT NULL,
        phone TEXT NOT NULL,
        capital TEXT,
        emoji TEXT,
        emojiU TEXT
    )
    """
    cur = con.cursor()
    cur.execute(create_table_query)