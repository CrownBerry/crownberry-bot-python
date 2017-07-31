FROM python:3.6
ADD . /bot
WORKDIR /bot
RUN pip3.6 install -r requirements.txt
CMD ["python3.6", "main.py"]