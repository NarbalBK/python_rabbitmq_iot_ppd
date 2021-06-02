import pika
import json
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
            tipo = method.routing_key.split(" - ")
            responseString = body.decode("utf-8")
            responseJson = json.loads(responseString)
            value = "{:.2f}".format(responseJson["value"])+self.get_metric(tipo[1])
            date = responseJson["date"]
            valueDate = value+" - "+date

            sensor_value.config(text=value)
            msg_box.insert(tk.END, valueDate)
            
        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)

        channel.start_consuming()

    def get_metric(self, tipo):
        if tipo == "Umidade":
            return "%"
        elif tipo == "Velocidade":
            return "m/s"
        return "ºC"

    
        


        