# отправка сообщений в Телеграм с помощью обыкновенных запросов POST

TOKEN = "1818338603:AAEv3AOttf2NqRSSphapItXr-ADv3sbL0tM"
BASE_URL = 'https://api.telegram.org'
CHAT_ID = 362857450

# Телеграм говорит нам, что мы можем собрать URL по некоторому правилу и отправка сообщения
# произойдет просто по переходу по нему

sender_url = "https://api.telegram.org/bot1818338603:AAEv3AOttf2NqRSSphapItXr-ADv3sbL0tM/sendMessage?chat_id=362857450" \
             "text=ТЕСТОВОЕ СОООБЩЕНИЕ"

f"{BASE_URL}/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={notification.message}"


