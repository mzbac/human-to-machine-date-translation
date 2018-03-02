# install docker-ce
```bash
#!/bin/bash
 
apt-get -y install \
  apt-transport-https \
  ca-certificates \
  curl
 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
 
add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"
 
apt-get update
 
apt-get -y install docker-ce
```
# build docker image and run
```bash 
#!/bin/bash
sudp docker build -t human-machine .
sudo docker run -p 8080:8080 human-machine
```
