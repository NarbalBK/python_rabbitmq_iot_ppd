import pika
import json

class MainInfoSensor:
    def __init__(self, nome, tipo):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='main_x', exchange_type='direct')

        messageJson = {'name':nome, "type":tipo}
        message = json.dumps(messageJson)
        channel.basic_publish(
            exchange='main_x', routing_key="main_key", body=message)
        print(" [x] Sent %r:%r" % ("main_key", message))

        connection.close()
        
        
