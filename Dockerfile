FROM ubuntu:latest


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
