import pika
import json

class MainInfoSensor:
    def __init__(self, nome, tipo, exchange, routing_key):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange=exchange, exchange_type='direct')

        messageJson = {'name':nome, "type":tipo}
        message = json.dumps(messageJson)
        channel.basic_publish(
            exchange=exchange, routing_key=routing_key, body=message)
        print(" [x] Sent %r:%r" % (exchange, message))

        connection.close()
        
        
