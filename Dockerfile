  
#Dockefile for creating a docker image : Ubuntu + Apache + Pyhton + Flask
# install mysql, python-pip, boto3, CSV
FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python python-pip wget gcc phantomjs firefox

RUN apt-get install -y xvfb

RUN apt-get install -y lynx

RUN apt-get install sudo 

RUN sudo apt install  -y apache2

RUN sudo apt install -y vim

RUN sudo apt install -y python-pip
RUN sudo apt-get install python3-mysql.connector
RUN sudo apt-get install -y python-boto3
RUN sudo apt-get install -y csvkit

EXPOSE 8000

WORKDIR  /RDS

ADD Excel_sql.py /RDS
RUN chmod +x /RDS/Excel_sql.py