FROM python:3.10 AS base
COPY ./consumer /consumer
COPY ./utils /consumer/utils
WORKDIR /consumer
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
RUN chmod +x start.sh
ENTRYPOINT ["/consumer/start.sh"]