FROM ubuntu:18.04
LABEL updated_at="2021-07-17" maintainer="takimotok"

# composer environment
ENV COMPOSER_ALLOW_SUPERUSER=1 \
  COMPOSER_HOME=/composer \
  PATH=$PATH:/composer/vendor/bin:/app/vendor/bin

# install libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
  python3.7 \
  python3-pip \
  vim

# set aliases
RUN echo "alias vi=/usr/bin/vim" >> ~/.bashrc && \
    echo "alias python=/usr/bin/python3.7"  >> ~/.bashrc && \
    echo "alias pip=/usr/bin/pip3" >> ~/.bashrc

# set application files and change working dir.
RUN mkdir -p /app
COPY ./index.py /app
WORKDIR /app
