FROM moxel/py3-pytorch
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip3 install Flask
RUN pip3 install http://download.pytorch.org/whl/cu80/torch-0.3.1-cp35-cp35m-linux_x86_64.whl 
RUN pip3 install torchvision
CMD ["python", "server.py"]
