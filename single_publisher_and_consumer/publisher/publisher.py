import os
import sys
from time import sleep

import pika

from utils.log import build_logger


logger = build_logger('Publisher')


def main():
    """ Producing messages """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(os.environ.get('AMQP_HOST'))
    )
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body='Hello World!'
    )
    logger.info("Sent 'Hello World!'")
    connection.close()


if __name__ == '__main__':
    try:
        logger.info('Producing message every 5 seconds. To exit press CTRL+C')
        while True:
            main()
            sleep(5)
    except KeyboardInterrupt:
        logger.info('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)