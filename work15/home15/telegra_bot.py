import telebot

from home15_1 import Customers, NotificationTasks, db
from secrets import token_hex

token = token_hex()
print(token)

api_telegram = '1517223699:AAG4JUoO3NMfiOoch9WkDuTa4MDdQ4g-csk'
bot = telebot.TeleBot(api_telegram)


@bot.message_handler(commands=['start'])
def welcome(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, 'Hello, ' + str(name))


@bot.message_handler(commands=["subscribe_me"])
def subscribe_profile(message):
    profile = Customers.query.get(int(message.text.split()[1]))
    profile.is_subscribed = True
    profile.profile_tg_chat_id = message.chat.id
    db.session.commit()


@bot.message_handler(commands=["unsubscribe_me"])
def unsubscribe_profile(message):
    profile = Customers.query.get(int(message.text.split()[1]))
    profile.is_subscribed = False
    profile.profile_tg_chat_id = None
    db.session.commit()


def order_create(message):
    name = message.from_user.first_name
    bot.reply_to(message, str(name) + ', Create your order: ')
    order_add = NotificationTasks(name=message.text, notification_task_id=message.chat.id,
                                  message=message.text, create_dt=message.dt)
    db.session.add(order_add)
    db.session.flush()
    db.session.commit()
    bot.reply_to(message, 'Order created')


@bot.message_handler(commands=['create'])
def order_message(message):
    custom = [i.c_name for i in Customers.query.all()]
    if message.from_user.first_name not in custom:
        user = Customers(c_name=message.from_user.first_name, phone=message.text, create_dt=message.dt,
                         chat_id=message.chat.id)
        db.session.add(user)
        db.session.commit()
        bot.send_message(chat_id=message.chat.id, text="Register")
    else:
        bot.send_message(chat_id=message.chat.id, text="Registered in base")

    bot.register_next_step_handler(message, order_create)


cnt = 0


def my_shiny_func(message):
    global cnt
    if cnt < 1:
        print("Я принял сообщение!")
        bot.reply_to(message=message, text=f"{message.from_user.first_name}, ты выбрал {message.text}")
        bot.register_next_step_handler(message, my_shiny_func)
        cnt += 1


def planner(message):
    print(f"Для нового дня: {message.text}")


@bot.message_handler(commands=["planner"])
def echo(message):
    global cnt
    cnt = 0
    bot.reply_to(message=message, text=f"{message.from_user.first_name}, давай запланируемся на 3 дней?")
    bot.register_next_step_handler(message, my_shiny_func)


@bot.message_handler(commands=["echo"])
def echo(message):
    bot.reply_to(message=message, text=f"{message.from_user.first_name}, выбери одно из двух: заявки или инфо?")
    bot.register_next_step_handler(message, my_shiny_func)


def notify(chat_id):
    message_to_send = input("Введите сообщение для отправки пользователю: ")
    bot.send_message(chat_id=chat_id, text=message_to_send)


@bot.message_handler(commands=["notify_all"])
def notify_all(message):
    _, user_token = message.text.split()
    if user_token == token:
        print("Я пошел в базу данных и вытащил всех, кто подписан на уведомления")
        profiles = Customers.query.filter_by(is_subscribed=True)
        for profile in profiles:
            notify(chat_id=profile.profile_tg_chat_id)


if __name__ == "__main__":
    bot.polling()
