import sqlite3
rule_for_table = False

def create_datatable_for_gpt():
    global rule_for_table
    connection = sqlite3.connect('technic_data.db', timeout=20)
    cur = connection.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS gpt_technic_base(
        numb INTEGER,
        all_tokens INTEGER, 
        users INTEGER,
        iam_token TEXT
        );
    '''
    cur.execute(query)
    connection.commit()
    connection.close()
    if not rule_for_table:
        create_table_new()
        rule_for_table = True

def create_table_new():
    connection = sqlite3.connect('technic_data.db', timeout=20)
    cur = connection.cursor()
    cur.execute(
        'INSERT INTO gpt_technic_base VALUES(?, ?, ?, ?);',
        (1, 0, 0, "d")
    )
    connection.commit()
    connection.close()

def tokens():
    connection = sqlite3.connect('technic_data.db')
    cur = connection.cursor()
    query = f'SELECT all_tokens FROM gpt_technic_base WHERE numb = 1;'
    results = cur.execute(query).fetchone()
    connection.close()
    if results != 0:
        return results[0]
    else:
        return

def new_tokens(command):
    connection = sqlite3.connect('technic_data.db')
    cur = connection.cursor()
    cur.execute(
        'UPDATE gpt_technic_base SET all_tokens = ? WHERE numb = 1;',
        (command)
    )
    connection.commit()
    connection.close()

def users_eye():
    connection = sqlite3.connect('technic_data.db')
    cur = connection.cursor()
    query = f'SELECT users FROM gpt_technic_base WHERE numb = 1;'
    results = cur.execute(query).fetchone()
    connection.close()
    try:
        if results[0] != 0:
            return results[0]
        else:
            return 0
    except:
        return 0

def us_plus():
    users_in_table = users_eye()
    connection = sqlite3.connect('technic_data.db')
    cur = connection.cursor()
    cur.execute(
        'UPDATE gpt_technic_base SET users = ? WHERE numb = 1;',
        ((users_in_table + 1), )
    )
    connection.commit()
    connection.close()

def iam_tokens():
    connection = sqlite3.connect('technic_data.db')
    cur = connection.cursor()
    query = f'SELECT iam_token FROM gpt_technic_base WHERE numb = 1;'
    results = cur.execute(query).fetchone()
    connection.close()
    if results != 0:
        return results[0]
    else:
        return

def new_iam_token(command):
    connection = sqlite3.connect('technic_data.db')
    cur = connection.cursor()
    cur.execute(
        'UPDATE gpt_technic_base SET iam_token = ? WHERE numb = 1;',
        (command,)
    )
    connection.commit()
    connection.close()

def clear_users_base():
    connection = sqlite3.connect('technic_data.db.db')
    cur = connection.cursor()
    cur.execute('DELETE users FROM users_base WHERE numb = 1;')
    connection.commit()
    connection.close()