FROM ubuntu:14.04.4


RUN apt-get update && apt-get install -y apt-transport-https
RUN echo 'deb http://private-repo-1.hortonworks.com/HDP/ubuntu14/2.x/updates/2.4.2.0 HDP main' >> /etc/apt/sources.list.d/HDP.list
RUN echo 'deb http://private-repo-1.hortonworks.com/HDP-UTILS-1.1.0.20/repos/ubuntu14 HDP-UTILS main'  >> /etc/apt/sources.list.d/HDP.list
RUN echo 'deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/azurecore/ trusty main' >> /etc/apt/sources.list.d/azure-public-trusty.list


ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update
RUN apt-get install -y 	python3 \
			python3-pip \
			npm \
			telnet \
			curl

RUN apt-get install -y 	make \
			g++ \
			libssl-dev \
			git \
			vim

RUN npm install -g yarn

RUN apt-get install pipx
RUN pipx ensurepath

EXPOSE 5000
