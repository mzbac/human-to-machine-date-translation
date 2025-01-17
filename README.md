# Getting started
```
git clone https://github.com/mzbac/human-to-machine-date-translation.git
```
# [live demo](https://qx2wv8xp1.firebaseapp.com/)

# docker env
```bash
#!/bin/bash
cd host
docker build -t human-machine .
docker run -p 8080:8080 human-machine
```
# cloud setting
- select Deep Learning AMI (Ubuntu) Version 4.0 - ami-b40f8bcc
- ssh to remote ec2
- source activate pytorch_p36

# Serving model 
```
cd host
flask run
```
browse to `localhost:8080/?date= 2 apr 2018`, see translated date format

# Requirements 
- python 3
- pytorch
- flask
