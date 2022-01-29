FROM python:3.10 AS base
COPY ./publisher /publisher
COPY ./utils /publisher/utils
WORKDIR /publisher
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
RUN chmod +x start.sh
ENTRYPOINT ["/publisher/start.sh"]