import requests
import time
from database import *
from commands import *
from database_gpt import *

MAX_PROJECT_TOKENS = 15000

folder_id = 'b1g8ttv0k823647abdcg'

def ask_gpt(text, user_id):
    # try:
        if tokens() < 15000:
            scripttext = iam_tokens()
            if timez() < time.time():
                create_new_token()
                timez_new(time.time() + scripttext["expires_in"])
            iam_token = scripttext["access_token"]
            system_content = content_for_user(user_id)
            headers = {
                'Authorization': f'Bearer {iam_token}',
                'Content-Type': 'application/json'
            }
            data = {
                "modelUri": f"gpt://{folder_id}/yandexgpt-lite",  # модель для генерации текста
                "completionOptions": {
                    "stream": False,  # потоковая передача частично сгенерированного текста выключена
                    "temperature": 0.6,  # чем выше значение этого параметра, тем более креативными будут ответы модели (0-1)
                    "maxTokens": "200"  # максимальное число сгенерированных токенов, очень важный параметр для экономии токенов
                },
                "messages": [
                    {
                        "role": "user",  # пользователь спрашивает у модели
                        "text": text  # передаём текст, на который модель будет отвечать
                    },
                    {
                        "role": "system",
                        "text": system_content
                    }
                ]
            }

            # Выполняем запрос к YandexGPT
            response = requests.post("https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                                     headers=headers,
                                     json=data)

            # Проверяем, не произошла ли ошибка при запросе
            if response.status_code == 200:
                text = response.json()["result"]["alternatives"][0]["message"]["text"]
                # a = tokens() + len(text)
                # new_tokens(a)
                return text
        else:
            return "К сожалению токены закончились :("
    # except:
    #     return "гпт не работает, возможно стоит попробовать команду /key для обновления токена."

    # else:
    #     raise RuntimeError(
    #         'Invalid response received: code: {}, message: {}'.format(
    #             {response.status_code}, {response.text}
    #         )
    #     )


# def tokens():
