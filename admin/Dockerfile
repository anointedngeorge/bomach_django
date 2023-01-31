FROM python:3.10.1

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Only update packages
RUN apt-get update

# Set working directory
WORKDIR /admin

# upgrade pip to latest
RUN pip3 install --upgrade pip

# copy requirements files
COPY ./requirements.txt /admin/requirements.txt


# install requirements
RUN pip3 install -r requirements.txt

# Copy codebase
COPY . /admin/

# create a new user
# RUN adduser --disabled-password --gecos '' bomach_django

# EXPOSE 8000

# Set user as the owner of the main directory
# RUN chown -R bomach_django:bomach_django /admin

# Set user to be bomach
# USER bomach_django
