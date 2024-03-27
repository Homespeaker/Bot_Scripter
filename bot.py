import telebot
import logging
from database import *
from commands import *
from database_gpt import *
create_datatable_for_gpt()
from gpt import *
import time

bot = telebot.TeleBot('6182241691:AAFl3lahEdNLQGp3hurvMI8JeYbAIRlHc54')
create_datatable_for_gpt()
create_datatable()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start - старт, что тут спрашивать\n"
                                      "/clear_users_base - очистить количество пользователей взаимодействующих с ботом\n"
                                      "/clear_base - полная очистка базы пользователей")

@bot.message_handler(commands=['start'])
def start(message):
    try:
        logging.info("Отправка приветственного сообщения")
        if users_eye() < 4 or user_in_table(message.from_user.id):
            user_reg(message.from_user.id)
            if not user_in_table(message.from_user.id):
                us_plus()
            try:
                user_ses(content_ses(message.from_user.id) + 1, message.from_user.id)
            except:
                user_ses(1, message.from_user.id)
            bot.send_message(message.chat.id, "Привет!")
            if content_ses(message.from_user.id) == 4:
                bot.send_message(message.chat.id, "К сожалению у тебя не осталось сессий.")
            else:
                if content_ses(message.from_user.id) == 0:
                    bot.send_message(message.chat.id, "Учти, что на пользование ботом у тебя есть всего три сессии по три вопроса, "
                                                      "израсходовав которые у тебя будет закрыт доступ.")
                else:
                    bot.send_message(message.chat.id, f"У тебя осталось {3 - content_ses(message.from_user.id)}")
                bot.send_message(message.chat.id, "Я твой помощник для написания сценариев.")
                bot.send_message(message.chat.id, 'Для начала выбери жанр произведения из данных ниже.')
                bot.send_message(message.chat.id, "Для выбора жанра нажми на одну из команд: "
                                                  "/comedy - комедия, /tragedia - трагедия, /povest - повесть")

        else:
            bot.send_message(message.chat.id, "К сожалению все тестирующие места заняты, обратитесь к администратору.")
    except:
        bot.send_message(message.chat.id, 'Возникла ошибка в поле start')
        logging.debug(f"Возникла ошибка в поле start")


@bot.message_handler(commands=['clear_users_base'])
def clear_users_base(message):
    clear_users_bas()
    bot.send_message(message.chat.id, "Количество пользователей очищено, открыт полный доступ к базе.")

@bot.message_handler(commands=['clear_base'])
def clear(message):
    clear_base()
    bot.send_message(message.chat.id, "База очищена")


@bot.message_handler(commands=['comedy'])
def comedy(message):
    bot.send_message(message.chat.id, "Отлично, ты выбрал жанр.")
    bot.send_message(message.chat.id, "Теперь выбери главного персонажа твоего рассказа.")
    bot.send_message(message.chat.id, "Для выбора главного героя нажми на одну из комманд. "
                                      "/ivan - Иван Дурак, /dart_veider - Дарт Вейдер, /yasher - Ящер, /homiak - Хомяк.")
    janr('comedy', message.from_user.id)

@bot.message_handler(commands=['tragedia'])
def tragedia(message):
    bot.send_message(message.chat.id, "Отлично, ты выбрал жанр.")
    bot.send_message(message.chat.id, "Теперь выбери главного персонажа твоего рассказа.")
    bot.send_message(message.chat.id, "Для выбора главного героя нажми на одну из комманд. "
                                      "/ivan - Иван Дурак, /dart_veider - Дарт Вейдер, /yasher - Ящер, /homiak - Хомяк.")
    janr('tragedia', message.from_user.id)

@bot.message_handler(commands=['povest'])
def povest(message):
    bot.send_message(message.chat.id, "Отлично, ты выбрал жанр.")
    bot.send_message(message.chat.id, "Теперь выбери главного персонажа твоего рассказа.")
    bot.send_message(message.chat.id, "Для выбора главного героя нажми на одну из комманд. "
                                      "/ivan - Иван Дурак, /dart_veider - Дарт Вейдер, /yasher - Ящер, /homiak - Хомяк.")
    janr('povest', message.from_user.id)

@bot.message_handler(commands=['ivan'])
def ivan(message):
    bot.send_message(message.chat.id, "Отлично, ты выбрал главного героя.")
    bot.send_message(message.chat.id, "Теперь выбери вселенную, где будут происходить события.")
    bot.send_message(message.chat.id, "Для выбора вселенной нажми на одну из комманд. "
                                      "/marvel - Марвел, /dc - DC, /stalker - Сталкер")
    name('ivan', message.from_user.id)

@bot.message_handler(commands=['dart_veider'])
def dart_veider(message):
    bot.send_message(message.chat.id, "Отлично, ты выбрал главного героя.")
    bot.send_message(message.chat.id, "Теперь выбери вселенную, где будут происходить события.")
    bot.send_message(message.chat.id, "Для выбора вселенной нажми на одну из комманд. "
                                      "/marvel - Марвел, /dc - DC, /stalker - Сталкер")
    name('dart_veider', message.from_user.id)

@bot.message_handler(commands=['yasher'])
def yasher(message):
    bot.send_message(message.chat.id, "Отлично, ты выбрал главного героя.")
    bot.send_message(message.chat.id, "Теперь выбери вселенную, где будут происходить события.")
    bot.send_message(message.chat.id, "Для выбора вселенной нажми на одну из комманд. "
                                      "/marvel - Марвел, /dc - DC, /stalker - Сталкер")
    name('yasher', message.from_user.id)

@bot.message_handler(commands=['homiak'])
def homiak(message):
    bot.send_message(message.chat.id, "Отлично, ты выбрал главного героя.")
    bot.send_message(message.chat.id, "Теперь выбери вселенную, где будут происходить события.")
    bot.send_message(message.chat.id, "Для выбора вселенной нажми на одну из комманд. "
                                      "/marvel - Марвел, /dc - DC, /stalker - Сталкер")
    name('homiak', message.from_user.id)

@bot.message_handler(commands=['marvel'])
def marvel(message):
    bot.send_message(message.chat.id, "Отлично, ты выбрал вселенную, где уже скоро развернутся события твоего сценария.")
    bot.send_message(message.chat.id, "Теперь, если ты хочешь дополнить сценарий какими то дополнительными подробностями, "
                                      "просто напиши их мне, или нажми на команду /start_the_generating в случае, если нету никаких дополнений.")
    verse('marvel', message.from_user.id)

@bot.message_handler(commands=['dc'])
def dc(message):
    bot.send_message(message.chat.id, "Отлично, ты выбрал вселенную, где уже скоро развернутся события твоего сценария.")
    bot.send_message(message.chat.id, "Теперь, если ты хочешь дополнить сценарий какими то дополнительными подробностями, "
                                      "просто напиши их мне, или нажми на команду /start_the_generating в случае, если нету никаких дополнений.")
    verse('dc', message.from_user.id)

@bot.message_handler(commands=['stalker'])
def stalker(message):
    bot.send_message(message.chat.id, "Отлично, ты выбрал вселенную, где уже скоро развернутся события твоего сценария.")
    bot.send_message(message.chat.id, "Теперь, если ты хочешь дополнить сценарий какими то дополнительными подробностями, "
                                      "просто напиши их мне, или нажми на команду /start_the_generating в случае, если нету никаких дополнений.")
    verse('stalker', message.from_user.id)

@bot.message_handler(commands=['all_story'])
def all_story(message):
    try:
        bot.send_message(message.chat.id, question_us(message.from_user.id))
        bot.send_message(message.chat.id, "Теперь нажми /start для генераций новых запросов.")
    except:
        bot.send_message(message.chat.id, 'Возникла ошибка в поле all_story')
        logging.debug(f"Возникла ошибка в поле all_story")

@bot.message_handler(commands=['tokens'])
def tokens(message):
    try:
        bot.send_message(message.chat.id, f"Количество потраченных токенов - {tokens()}")
        bot.send_message(message.chat.id, f"Количество оставшихся токенов - {13000 - tokens()}")
    except:
        bot.send_message(message.chat.id, 'Возникла ошибка в поле tokens')
        logging.debug(f"Возникла ошибка в поле tokens")

@bot.message_handler(commands=['start_the_generating'])
def strt_gen(message):
    # try:
        if check_verse(message.from_user.id) and check_name(message.from_user.id) and check_janr(message.from_user.id):
            if content_ses(message.from_user.id) < 4:
                logging.debug(f"Первый ввод, без слов")
                bot.send_message(message.chat.id, "Окей, начинаю генерацию твоего запроса.")
                user_question("Напиши сценарий.", message.from_user.id)
                if content_num(message.from_user.id) == 0:
                    text = ask_gpt("напиши сценарий", message.from_user.id)
                    bot.send_message(message.chat.id, text)
                    user_question("//Напиши сценарий.// " + ask_gpt(question_us(message.from_user.id), message.from_user.id), message.from_user.id)
                    bot.send_message(message.chat.id,
                                     'Теперь ты можешь внести правки в сценарий, или попросить меня его продолжить.')
                    bot.send_message(message.chat.id,
                                     'В случае если ты хочешь создать новый сценарий просто нажми /start.')
                    user_num(1, message.from_user.id)
            else:
                bot.send_message(message.chat.id, 'К сожалению вы потратили все доступные сессии, для повторного обращения '
                                                  'свяжитесь с администратором бота или дождитесь его обновления.')
        else:
            bot.send_message(message.chat.id, 'Сначала нажми /start и полностью пройди процесс моей настройки.')
    # except:
    #     bot.send_message(message.chat.id, 'Возникла ошибка в поле start_the_generating')
    #     logging.debug(f"Возникла ошибка в поле start_the_generating")


@bot.message_handler(content_types=['text'])
def text_for_gpt(message):
    try:

        if content_ses(message.from_user.id) < 4:
            if check_verse(message.from_user.id) and check_name(message.from_user.id) and check_janr(message.from_user.id):
                logging.debug(f"Полученный текст от пользователя: {message.text}, все гуд")
                if content_num(message.from_user.id) == 0:
                    user_question("//" + message.text + "//", message.from_user.id)
                    text = ask_gpt(question_us(message.from_user.id), message.from_user.id)
                    bot.send_message(message.chat.id, text)
                    user_question(question_us(message.from_user.id) + " " + text, message.from_user.id)
                    print(question_us(message.from_user.id))
                    bot.send_message(message.chat.id,
                                     'Теперь ты можешь внести правки в сценарий, или попросить меня его продолжить.')
                    bot.send_message(message.chat.id,
                                     'В случае если ты хочешь создать новый сценарий просто нажми /start.')
                    user_num(1, message.from_user.id)
                elif content_num(message.from_user.id) == 1:
                    user_question(question_us(message.from_user.id) + " " + "//" + message.text + "//", message.from_user.id)
                    text = ask_gpt(question_us(message.from_user.id), message.from_user.id)
                    bot.send_message(message.chat.id, ask_gpt(question_us(message.from_user.id), message.from_user.id))
                    user_question(question_us(message.from_user.id) + " " + text, message.from_user.id)
                    print(question_us(message.from_user.id))
                    bot.send_message(message.chat.id,
                                     'Теперь ты можешь внести правки в сценарий, или попросить меня его продолжить.')
                    bot.send_message(message.chat.id,
                                     'В случае если ты хочешь создать новый сценарий просто нажми /start. '
                                     'Если ты хочешь посмотреть полностью сгенерированную историю нажми  /all_story')
                    user_num(2, message.from_user.id)
                elif content_num(message.from_user.id) == 2:
                    user_question(question_us(message.from_user.id) + " " + "//" + message.text + "//", message.from_user.id)
                    text = ask_gpt(question_us(message.from_user.id), message.from_user.id)
                    bot.send_message(message.chat.id, ask_gpt(question_us(message.from_user.id), message.from_user.id))
                    print(question_us(message.from_user.id))
                    user_question(question_us(message.from_user.id) + " " + text, message.from_user.id)
                    user_num(3, message.from_user.id)
                    bot.send_message(message.chat.id, "На этом количество вопросов в этой сессии закончилось, просьба создать"
                                                      " новую сессию если у вас остались вопросы. Для этого нажмите /start. "
                                                      "Если вы хотите прочитать полностью сгенерированную историю, то нажмите"
                                                      " /all_story")
                else:
                    bot.send_message(message.chat.id, "К сожалению вопросы для данной сесси закончились, для новых вопросов "
                                                      "создайте новую сессию. Если вы хотите прочитать полностью сгенерированную историю, то нажмите"
                                                      " /all_story")
            else:
                bot.send_message(message.chat.id, 'Сначала нажми /start и полностью пройди процесс моей настройки.')
        else:
            bot.send_message(message.chat.id, 'К сожалению вы потратили все доступные сессии, для повторного обращения '
                                              'свяжитесь с администратором бота или дождитесь его обновления.')
    except:
        bot.send_message(message.chat.id, 'Возникла ошибка в поле text')
        logging.debug(f"Возникла ошибка в поле text")




bot.polling()
