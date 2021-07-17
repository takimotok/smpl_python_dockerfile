# Sample Docker file for learning Python3.x

This is the sample repository for learning Python3.x .

The Docker file :

- use ubuntu:18.04 image
- use libraries:
  - pip
  - vim
- set some aliases:
  - vi
  - python
  - pip
- set working directory as `/app`
- mount `index.py` into `/app/here`


## Usage

Build the image.

```
$ docker build \
  --no-cache \
  -t takimotok/ubuntu:18.04 \
  -f ./Dockerfile .
```

Run container.

```
$ docker run --name=py -it takimotok/ubuntu:18.04 /bin/bash
```
