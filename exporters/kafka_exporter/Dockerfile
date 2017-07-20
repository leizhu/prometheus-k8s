FROM ubuntu:14.04

MAINTAINER lei.zhu.1017@gmail.com

COPY sources.list /etc/apt/sources.list

#RUN apt-get update && apt-get -y install wget

# install jdk 
RUN mkdir -p /tmp/sps
COPY java_1.8.0_45.deb /tmp/sps
RUN dpkg -i /tmp/sps/java_1.8.0_45.deb && \
        rm -rf /skyguard-jre && rm -rf /tmp/sps

# environment
ENV JAVA_HOME /usr/skyguardtools/java
ENV JRE_HOME /usr/skyguardtools/java/jre
ENV PATH $JAVA_HOME/bin:$JRE_HOME/bin:$PATH
ENV CLASSPATH /usr/skyguardtools/java/lib:/usr/skyguardtools/java/jre/lib

WORKDIR /opt
COPY ./kafka_consumer_group_exporter /opt/
COPY kafka_2.11-0.10.0.0 /opt/kafka

EXPOSE 7979

ENTRYPOINT [ "/opt/kafka_consumer_group_exporter", "--consumer-group-command-path=/opt/kafka/bin/kafka-consumer-groups.sh", "kafka" ]
