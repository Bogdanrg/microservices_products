import pika
import json

params = pika.URLParameters('amqps://rtuvvmuv:yuKq5YflGgxXdCw8e03fr8g67Fo4eTe-@jackal.rmq.cloudamqp.com/rtuvvmuv')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
