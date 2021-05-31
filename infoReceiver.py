import pika
import tkinter as tk

class InfoReceiver:
    def __init__(self, exchange, routing_key, sensor_value, msg_box):

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange=exchange, exchange_type='direct')

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue    

        channel.queue_bind(
                exchange=exchange, queue=queue_name, routing_key=routing_key) 
        
        print(' [*] Waiting for {}'.format(routing_key))

        def callback(ch, method, properties, body):
            print(" [x] %r:%r" % (method.routing_key, body))
            
        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)

        msg_box.insert(tk.END, "ABEL") #TESTE
            
        channel.start_consuming()

    
        


        