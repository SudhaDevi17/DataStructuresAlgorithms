#Deriving the latest base image
FROM python:latest as base

#Labels as key value pair
LABEL Maintainer="sudha.devi"

FROM base as test

#to COPY the remote file at working directory in container
COPY . .

CMD [ "python", "-m", "unittest"]