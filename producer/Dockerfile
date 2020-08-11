# Dockerfile
FROM python:3.6

WORKDIR /usr/app

ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./

# Creating topic

# Run Producer Script
CMD ["./run.sh"]
