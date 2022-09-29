def cont_insert(continent_dict, country_code, cont_table, con):
    query = f"""INSERT INTO {cont_table}(
        country_code,
        code,
        name
    )
    VALUES (
        :country_code,
        :code,
        :name
    )
    """
    continent_dict.update({'country_code': country_code})
    cur = con.cursor()
    cur.execute(query, continent_dict)

def lang_insert(languages_list, country_code, lang_table, con):
    for language_dict in languages_list:
        query = f"""INSERT INTO {lang_table}(
            country_code,
            code,
            name,
            native,
            rtl
        )
        VALUES (
            :country_code,
            :code,
            :name,
            :native,
            :rtl
        )
        """
        language_dict.update({'country_code': country_code})
        cur = con.cursor()
        cur.execute(query, language_dict)


def curr_insert(currency_str, country_code, curr_table, con):
    curr_list = currency_str.split(',') if currency_str else [None]
    for curr in curr_list:
        query = f"""INSERT INTO {curr_table}(
            country_code,
            currency
        )
        VALUES (
            :country_code,
            :currency
        )
        """
        currency_dict = {'country_code': country_code, 'currency': curr}
        cur = con.cursor()
        cur.execute(query, currency_dict)

def ctry_insert(country_dict, cont_table, con):
    query = f"""INSERT INTO {cont_table}(
        code,
        name,
        native,
        phone,
        capital,
        emoji,
        emojiU
    )
    VALUES (
        :code,
        :name,
        :native,
        :phone,
        :capital,
        :emoji,
        :emojiU
    )
    """
    cur = con.cursor()
    cur.execute(query, country_dict)