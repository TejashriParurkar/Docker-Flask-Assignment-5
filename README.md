# Docker-Flask-Assignment-5

This project contains Dockerized Flask API
(Createf python flask RESTul API and used docker to run this application.)

1. Created a flask RESTful API.
   Refer the following link : https://www.youtube.com/watch?v=s_ht4AKnWZg
   A. Used jinja templating for python.

2. Dockerized it.
   Refer the following link : https://www.youtube.com/watch?v=prlixoDIfrc&t=1233s
  A. Docker needs to installed.
     Refer the following link : https://www.docker.com/products/docker-desktop
  B. Run the following commands :
      1. $ docker build -t flask-sample-test .
         (build the docker image)
      2. $ docker run -d -p 5000:5000 flask-sample-test
         (once docker image is created, ruun the "flask-sample-test" in docker container)
      3. $ docker run -it flask-sample-test 
         (run it)
  C. Now, the App will run locally. i.e if it run on normal termial, address will be localhost else docker ip address.
  
  
  
  
