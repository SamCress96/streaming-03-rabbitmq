"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Samantha Cress
    Date: January 31, 2023

"""

# add imports at the beginning of the file
import pika
# create a blocking connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# use the connection to create a communication channel
channel = connection.channel()
# use the channel to declare a queue
channel.queue_declare(queue='Hello')
channel.queue_declare(queue='My')
channel.queue_declare(queue='I')
channel.queue_declare(queue='This')
# use the channel to publish a message to the queue
channel.basic_publish(exchange='', routing_key='Hello', body='Hello World!')
channel.basic_publish(exchange='', routing_key='My', body='My name is Sam!')
channel.basic_publish(exchange='', routing_key='I', body='I have a lizard named Jeff!')
channel.basic_publish(exchange='', routing_key='This', body='This is pretty cool!')
# print a message to the console for the user
print(" [x] Sent 'Hello World!'")
print(" [x] Sent 'My name is Sam!'")
print(" [x] Sent 'I have a lizard named Jeff!'")
print(" [x] Sent 'This is pretty cool!'")
# close the connection to the server
connection.close()




