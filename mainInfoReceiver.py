import pika
import json

class MainInfoReceiver:
    def __init__(self, mainInterface, exchange, routing_key):

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange=exchange, exchange_type='direct')

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue    

        channel.queue_bind(
                exchange=exchange, queue=queue_name, routing_key=routing_key) 
        
        print(' [*] Waiting for logs. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            print(" [x] %r:%r" % (method.routing_key, body))
            responseString = body.decode("utf-8")
            responseJson = json.loads(responseString)
            name = responseJson["name"]
            tipo = responseJson["type"]
            nametype = name+" - "+tipo

            mainInterface.options.append(nametype)
            mainInterface.nametype[nametype] = tipo
            mainInterface.update_option_menu()

        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)
            
        channel.start_consuming()

       
    
        


        