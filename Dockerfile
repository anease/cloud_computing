FROM python:3.7-alpine

RUN cd /home; mkdir data

COPY . /home

CMD ["python3", "/home/docker_project.py"]
