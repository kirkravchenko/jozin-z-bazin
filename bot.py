from openai import OpenAI
import telebot
from sensitive import Sensitive

bot = telebot.TeleBot(Sensitive.tg_token, parse_mode='MARKDOWN')
client = OpenAI(api_key=Sensitive.openai_token)
model = Sensitive.model

@bot.message_handler()
def command_help(message):
    response = request_llm(message.text)
    bot.reply_to(message, response)


def request_llm(user_message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": Sensitive.prompt_1,
            },
            {
                "role": "system",
                "content": Sensitive.prompt_2,
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        model=model,
    )
    response = chat_completion.choices[0].message.content
    return response


print("bot is running...")
bot.infinity_polling()
