FROM python:3.11-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY .env /app/.env
COPY requirements.txt .
RUN apt update &&  \
    apt install -y libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
      libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
      libharfbuzz-dev libfribidi-dev libxcb1-dev &&  \
    rm -rf /var/lib/apt/lists/* && \ pip install --no-cache -r /app/requirements.txt
COPY mma_parser.py /app/mma_parser.py
COPY vk_parser.py /app/vk_parser.py
COPY cooc.py /app/cooc.py
COPY config.py /app/config.py
COPY bot.py /app/bot.py
CMD ["python", "-m", "bot"]
CMD ["python", "-m", "vk_parser"]
CMD ["python", "-m", "mma_parser"]
#LABEL autor=rgg
#RUN apt-get update
#RUN apt-get install python
#WORKDIR /usr/local/
#COPY /usr/local/
#ENV owner='Administrator'
#EXPOSE 80
#ENTRYPOINT ['echo']
#CMD ['Hello my First Docker']
