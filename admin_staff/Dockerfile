FROM python:3.10.1
# FROM python:3.6-slim-buster AS build
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Only update packages
RUN apt-get update

# copy requirements files
# COPY ./requirements.txt /admin/requirements.txt
# Set working directory
WORKDIR /admin

# upgrade python pip
RUN pip3 install --upgrade pip
# upgrade pip to latest

# Copy codebase
COPY requirements.txt .
# install requirements
RUN pip3 install -r requirements.txt

COPY . .
# create a new user
# RUN adduser --disabled-password --gecos '' bomach_django

# EXPOSE 8000

# Set user as the owner of the main directory
# RUN chown -R bomach_django:bomach_django /customer_app

# Set user to be bomach
# USER bomach_django

