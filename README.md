### Assignment Notes

### Simple Consumer

### Instructions

#### 1. Reproducible environment

1. Create Network
    > `docker network create assignment-kafka-network`
1. Fire up Kafka Node
    > `docker-compose -f docker-compose.kafka.yml`

#### 2. Simple Consumer

1. Run Producer and Consumer
    > `docker-compose up`
1. Check output of `data-output`
    > `docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic data-output --from-beginning`

#### How to handle ordering ??

-   Idea: Storing data in KeyValue Store, Retreiving them in order
-   Saving them into Redis and retrieving sorted. and streaming to output

### 3. Scalable Consumer

### Resources

-   https://blog.cloudera.com/scalability-of-kafka-messaging-using-consumer-groups/
-   https://dev.to/florimondmanca/breaking-news-everything-is-an-event-streams-kafka-and-you-2n9j
-   https://www.cloudkarafka.com/blog/2018-08-21-faq-apache-kafka-strict-ordering.html
-   https://www.instaclustr.com/a-visual-understanding-to-ensuring-your-kafka-data-is-literally-in-order/
