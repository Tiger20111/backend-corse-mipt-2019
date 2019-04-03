import pika 

def send(email, url):
    conn_params = pika.ConnectionParameters('rabbit', 5672)
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()
    channel.queue_declare(queue='first-queue', durable=True)

    message = email + ' ' + url

    channel.basic_publish(exchange='', routing_key='queue',
                          body=message, properties=pika.BasicProperties(
                            delivery_mode = 2))
