import pika
import json

class MainInfoReceivier:
    def __init__(self, mainInterface):
        self.mainInterface = mainInterface

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

        channel = connection.channel()

        channel.exchange_declare(exchange='main_x', exchange_type='direct')

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue    
        
        channel.queue_bind(
                exchange='main_x', queue=queue_name, routing_key="main_key") 
        
        print(' [*] Waiting for logs. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            print(" [x] %r:%r" % (method.routing_key, body))
            responseString = body.decode("utf-8")
            responseJson = json.loads(responseString)
            name = responseJson["name"]
            tipo = responseJson["type"]
            nametype = name+" - "+tipo

            self.mainInterface.options.append(nametype)
            self.mainInterface.nametype[nametype] = tipo
            self.mainInterface.update_option_menu()

        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)
            
        channel.start_consuming()


        