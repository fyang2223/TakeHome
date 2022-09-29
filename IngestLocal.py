import requests
import sqlite3
import pandas as pd

URL = 'https://countries.trevorblades.com/'
TABLENAME = 'country'

def get_data():
    QUERY = '''
        query ($filter: CountryFilterInput) {
        countries(filter: $filter) {
            code
            name
            native
            phone
            continent {
                code
                name
            }
            capital
            currency
            languages {
                code
                name
                native
                rtl
            }
        }
    }
    '''
    VARIABLES = {
        "filter": {
            "code": {
            "regex": ".*"
            }
        }
    }

    r = requests.post(URL, json={'query': QUERY , 'variables': VARIABLES})
    response = r.json()
    return response

def create_table(con):
    CREATE_TABLE_QUERY = f"""
    CREATE TABLE IF NOT EXISTS {TABLENAME}(
        code TEXT NOT NULL,
        name TEXT NOT NULL,
        native TEXT NOT NULL,
        phone TEXT NOT NULL,
        continent_code TEXT,
        continent_name TEXT,
        capital TEXT,
        currency TEXT,
        languages_code TEXT,
        languages_name TEXT,
        languages_native TEXT,
        languages_rtl INTEGER
    )
    """
    cur = con.cursor()
    cur.execute(CREATE_TABLE_QUERY)

def input_data(con, response):
    for row in response.get('data',{}).get('countries',{}):
        row['languages'] = row['languages'] if row['languages'] else [{}]
        for lang in row['languages']:
            row.update({
                'languages_code': lang.get('code'),
                'languages_name': lang.get('name'),
                'languages_native': lang.get('native'),
                'languages_rtl': lang.get('rtl'),
                'continent_code': row.get('continent',{}).get('code'),
                'continent_name': row.get('continent',{}).get('name')
                })
        
            QUERY = f"""INSERT INTO {TABLENAME}(
                code,
                name,
                native,
                phone,
                continent_code,
                continent_name,
                capital,
                currency,
                languages_code,
                languages_name,
                languages_native,
                languages_rtl 
            )
            VALUES (
                :code,
                :name,
                :native,
                :phone,
                :continent_code,
                :continent_name,
                :capital,
                :currency,
                :languages_code,
                :languages_name,
                :languages_native,
                :languages_rtl
            )
            """
            cur = con.cursor()
            cur.execute(QUERY, row)

if __name__=='__main__':
    response = get_data()

    with sqlite3.connect("countries.db") as con:
        cur = con.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {TABLENAME}")

        create_table(con)
        input_data(con, response)
        
        df = pd.read_sql_query("SELECT * from country", con)
        df.to_parquet('output.parquet')









