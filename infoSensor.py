import pika
import json
import datetime

class InfoSensor:
    def __init__(self, exchange):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange=exchange, exchange_type='direct')
        self.channel = channel

        # connection.close()
        
    def sendMsg(self, value, exchange, routing_key):
        messageJson = {'value':value, "date":datetime.date.today()}
        message = json.dumps(messageJson)
        self.channel.basic_publish(
            exchange=exchange, routing_key=routing_key, body=message)
        print(" [x] Sent %r:%r" % (exchange, message))
        
