FROM ubuntu:16.04
RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get -y update

# Accept the license
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 boolean true" | debconf-set-selections

RUN apt-get -y install oracle-java8-installer

# Here comes the tomcat installation
RUN apt-get -y install tomcat8
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/default/tomcat8

# Expose the default tomcat port
EXPOSE 8080

# Start the tomcat (and leave it hanging)
CMD service tomcat8 start && tail -f /var/lib/tomcat8/logs/catalina.out
