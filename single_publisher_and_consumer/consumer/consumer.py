import os
import sys

import pika

from utils.log import build_logger


logger = build_logger('Consumer')


def callback(ch, method, properties, body):
    """ Confirmation of consumed message """
    logger.info(f'Received: {body}')


def main() -> None:
    """ Consuming messages """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(os.environ.get('AMQP_HOST'))
    )
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(
        queue='hello',
        auto_ack=True,
        on_message_callback=callback
    )
    logger.info('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
