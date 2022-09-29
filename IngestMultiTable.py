import requests
import sqlite3
import CreateTables
import IngestData

def get_countries_data(url):
    query = '''
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
            emoji
            emojiU
        }
    }
    '''
    variables = {
        "filter": {
            "code": {
            "regex": ".*"
            }
        }
    }

    r = requests.post(url, json={'query': query , 'variables': variables})
    response = r.json()
    return response







if __name__=='__main__':
    url = 'https://countries.trevorblades.com/'

    with sqlite3.connect("multitable_countries.db") as con:
        ctry_table = 'countries'
        cont_table = 'continents'
        lang_table = 'languages'
        curr_table = 'currency'

        response = get_countries_data(url)

        cur = con.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {ctry_table}")
        cur.execute(f"DROP TABLE IF EXISTS {cont_table}")
        cur.execute(f"DROP TABLE IF EXISTS {lang_table}")
        cur.execute(f"DROP TABLE IF EXISTS {curr_table}")

        CreateTables.create_ctry_table(con, ctry_table)
        CreateTables.create_cont_table(con, cont_table, ctry_table)
        CreateTables.create_lang_table(con, lang_table, ctry_table)
        CreateTables.create_curr_table(con, curr_table, ctry_table)

        for country in response.get('data',{}).get('countries'):
            country_code = country['code']

            continent_dict = country.get('continent')
            IngestData.cont_insert(continent_dict, country_code, cont_table, con)

            languages_list = country.get('languages')
            IngestData.lang_insert(languages_list, country_code, lang_table, con)

            currency_str = country.get('currency')
            IngestData.curr_insert(currency_str, country_code, curr_table, con)

            IngestData.ctry_insert(country, ctry_table, con)










