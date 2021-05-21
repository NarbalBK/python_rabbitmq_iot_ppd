#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='abel', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Abel Hello World!"
channel.basic_publish(exchange='abel', routing_key='', body=message)
print(" [x] Abel Sent %r" % message)
connection.close()