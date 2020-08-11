# Dockerfile
FROM python:3.6

WORKDIR /usr/app

ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./

# Creating topic
RUN python create_topic.py

# Run Producer Script
CMD ["python", "app.py"]
