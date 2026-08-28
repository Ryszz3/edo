import os
import environ
from edo.settings import BASE_DIR


def send_ai_request():
    env = environ.Env()
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    from openai import OpenAI

    client = OpenAI(
        api_key=env("PROXY_API_KEY"),
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    response = client.responses.create(
        model="gpt-4o",
        input="Привет!"
    )
    print(response)


def show_excel(request):
    pass



