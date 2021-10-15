FROM ubuntu:18.04
LABEL updated_at="2021-07-17" maintainer="takimotok"

# install libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
  cython \
  gcc \
  jq \
  libmysqlclient-dev \
  libpython3.7-dev \
  libxml2-utils \
  memcached \
  mysql-client \
  mysql-server \
  openjdk-8-jdk \
  python3-dev \
  python3-pip \
  python3-setuptools \
  python3.7 \
  sqlite3 \
  vim \
  wget

# pip が参照する python ver. (3.7) を揃える
RUN python3.7 -m pip install -U pip && \
  python3.7 -m pip install \
  Flask \
  PyMySQL \
  SQLAlchemy \
  happybase \
  mysql-connector-python \
  python-memcached \
  requests && \
  export PYTHONPATH="/usr/local/lib/python3/dist-packages:$PYTHONPATH" >> ~/.bashrc && \
  echo "alias vi=/usr/bin/vim" >> ~/.bashrc && \
  echo "alias python=/usr/bin/python3.7"  >> ~/.bashrc && \
  echo "alias sqlite=/usr/bin/sqlite3" >> ~/.bashrc

# set application files and change working dir.
RUN mkdir -p /app
COPY ./index.py /app
WORKDIR /app
