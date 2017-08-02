FROM crownberry/tensorflow-env:latest
ADD . /bot
WORKDIR /bot
CMD ["python3.6", "main.py"]