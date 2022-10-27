# init base images
FROM python:3.10.8

#create a folder in the image
WORKDIR /docker

# copy all the files in the local dir to image dir
ADD . /docker

#Upgarde pip
RUN pip install --upgrade pip

#run pip install all the requirements
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
EXPOSE 5000


