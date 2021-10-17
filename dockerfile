FROM ubuntu:20.04
ENV user=emailrbrb
ENV pwd=rbrbrb1!
ENV TO=rafaljbogusz@gmail.com
ENV FROM=rafalb
RUN apt-get -y -qq update
RUN apt-get -y -qq install curl
RUN apt-get -y  install python3
ADD https://raw.githubusercontent.com/rafalbog/crispy-11/main/email12345.py .
RUN python3 email12345.py
