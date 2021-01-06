FROM python:3

WORKDIR /usr/src/app
COPY . . 
CMD ["index.py"]
ENTRYPOINT ["python3"]