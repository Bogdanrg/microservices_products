import pika, json, os, django
from django.db.models import F

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()
from main.models import Product


params = pika.URLParameters('amqps://rtuvvmuv:yuKq5YflGgxXdCw8e03fr8g67Fo4eTe-@jackal.rmq.cloudamqp.com/rtuvvmuv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print("Received in admin")
    id = json.loads(body)
    product = Product.objects.filter(id=id).update(likes=F('likes') + 1)
    print('Product likes increased')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
