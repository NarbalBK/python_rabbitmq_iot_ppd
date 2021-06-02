import pika
import json
import datetime

class InfoSensor:
    def __init__(self, exchange, routing_key):
        self.exchange = exchange
        self.routing_key = routing_key

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange=exchange, exchange_type='direct')
        self.connection = connection
        self.channel = channel

        # connection.close()
        
    def sendMsg(self, value=""):
        dateTimeObj = datetime.datetime.now()
        timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        messageJson = {'value':value, "date":timestampStr}
        message = json.dumps(messageJson)
        self.channel.basic_publish(
            exchange=self.exchange, routing_key=self.routing_key, body=message)
        print(" [x] Sent %r:%r" % (self.exchange, message))

    def exit(self):
        self.connection.close()
        
