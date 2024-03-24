import sqlite3


def create_datatable():
    connection = sqlite3.connect('data.db', timeout=20)
    cur = connection.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS users_base(
        user_id INTEGER,
        janr TEXT,
        name TEXT,
        verse TEXT,
        user_question TEXT,
        number INTEGER,
        sessions INTEGER
        );
    '''

    cur.execute(query)
    connection.close()

def clear_base():
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    cur.execute('DELETE FROM users_base')
    connection.commit()
    connection.close()

def user_reg(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT user_id FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query)
    if results != user_id:
        cur.execute(f'DELETE FROM users_base WHERE user_id = {user_id}')
        cur.execute(
            'INSERT INTO users_base VALUES(?, ?, ?, ?, ?, ?, ?);',
            (user_id, 'ноун', 'ноун', 'ноун', 'ноун', 0, 0)
        )
    connection.commit()
    connection.close()

def janr(command, user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    cur.execute(
        'UPDATE users_base SET janr = ? WHERE user_id = ?;',
        (command, user_id)
    )
    connection.commit()
    connection.close()

def name(command, user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    cur.execute(
        'UPDATE users_base SET name = ? WHERE user_id = ?;',
        (command, user_id)
    )
    connection.commit()
    connection.close()

def verse(command, user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    cur.execute(
        'UPDATE users_base SET verse = ? WHERE user_id = ?;',
        (command, user_id)
    )
    connection.commit()
    connection.close()

def user_question(command, user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    cur.execute(
        'UPDATE users_base SET user_question = ? WHERE user_id = ?;',
        (command, user_id)
    )
    connection.commit()
    connection.close()

def check_janr(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT janr FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query)
    if results != 'ноун':
        connection.close()
        return True
    else:
        connection.close()
        return False

def check_name(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT name FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query)
    if results != 'ноун':
        connection.close()
        return True
    else:
        connection.close()
        return False

def check_verse(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT verse FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query)
    if results != 'ноун':
        connection.close()
        return True
    else:
        connection.close()
        return False

def check_num(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT number FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query)
    if results != 0:
        connection.close()
        return True
    else:
        connection.close()
        return False

def content_num(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT number FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query).fetchone()
    connection.close()
    if results != 0:
        return results[0]
    else:
        return

def user_num(command, user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    cur.execute(
        'UPDATE users_base SET number = ? WHERE user_id = ?;',
        (command, user_id)
    )
    connection.commit()
    connection.close()

def content_janr(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT janr FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query).fetchone()
    connection.close()
    if results != 'ноун':
        return results[0]
    else:
        return

def content_name(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT name FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query).fetchone()
    connection.close()
    if results != 'ноун':
        return results[0]
    else:
        return

def content_verse(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT verse FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query).fetchone()
    connection.close()
    if results != 'ноун':
        return results[0]
    else:
        return

def question_us(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT user_question FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query).fetchone()
    connection.close()
    if results != 'ноун':
        return results[0]
    else:
        return

def content_for_user(user_id):
    txt = "Ты дружелюбный бот помощник для написания сценариев. Как только ты видишь слово" \
          " выделенное таким образом //слово// это означает что пользователь вводит правки в твой сценарий. " \
          "Когда ты помогаешь пользователю писать сценарий не используй технических слов по типу 'сцена 1' " \
          "'персонажи'. Также хочу уточнить, что предложения нужно писать кратко. " \
          "Если тебе приходит просьба о продолжении сценария, то пиши его, а не начинай перепечатывать историю сначала. " \
          "Помни, ты пишешь историю вместе с пользователем в формате диалога. Жанр сегодняшнего сценария это "
    janr = ""
    name_charaster = ""
    verse_of_script = ""


    if content_janr(user_id) == 'comedy':
        janr = "комедия"
    elif content_janr(user_id) == 'tragedia':
        janr = "трагедия"
    elif content_janr(user_id) == 'povest':
        janr = "повесть"


    if content_name(user_id) == 'ivan':
        name_charaster = "Иван Дурак"
    elif content_name(user_id) == 'dart_veider':
        name_charaster = "Дарт Вейдер"
    elif content_name(user_id) == 'yasher':
        name_charaster = "Ящер"
    elif content_name(user_id) == 'homiak':
        name_charaster = "Хомяк"


    if content_verse(user_id) == 'marvel':
        verse_of_script = "Марвел"
    elif content_verse(user_id) == 'dc':
        verse_of_script = "DC"
    elif content_verse(user_id) == 'stalker':
        verse_of_script = "Сталкер"


    return f"Ты дружелюбный бот помощник для написания сценариев. Жанр сегодняшнего сценария это {janr}. " \
           f"Наш главный герой это {name_charaster}. Вселенная где будут происходить действия это {verse_of_script}."







def check_ses(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT sessions FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query)
    if results != 0:
        connection.close()
        return True
    else:
        connection.close()
        return False

def content_ses(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT sessions FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query).fetchone()
    connection.close()
    if results[0] != 0:
        return results[0]
    else:
        return

def user_ses(command, user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    cur.execute(
        'UPDATE users_base SET sessions = ? WHERE user_id = ?;',
        (command, user_id)
    )
    connection.commit()
    connection.close()


def user_in_table(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT user_id FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query).fetchone()
    connection.close()
    if results != user_id:
        return False
    else:
        return True


