import pika

from pika import PlainCredentials

# это просто синтаксис для создания подключения к Кролику
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost', credentials=PlainCredentials("rmquser", "rmqpass")))

# создаём канал для передачи данных
channel = connection.channel()

# channel.basic_publish(exchange='',  # это точка доступа к очередям (почтамт)
#                       routing_key='test_queue',  # это название очереди, куда отправляем сообщение
#                       body=b'Hello World!')
# print(" [x] Sent 'Hello World!'")

for num in range(100):
    channel.basic_publish(exchange='',
                          routing_key='test_queue',
                          body=f'{num}'.encode())
    print(f" [x] Sent '{num}'")

connection.close()