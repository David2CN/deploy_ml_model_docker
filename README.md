# Deploying an API service using Docker


## Build the image
```bash 
docker build -t <image_name>:<version> .
```
for example:
```bash 
docker build -t flower:v1 .
```

## Run the container
```bash
docker run --rm -p 80:80 <image_name>:<version>
```

for example:
```bash
docker run --rm -p 80:80 flower:v1
```
The above command spins up the model server.
Go to the built-in FastAPI client [docs](http://localhost:80/docs) to interact with the server.

You can also access the server with a curl command, like so:
```bash
curl -X 'POST' http://localhost/predict \
-H 'Content-Type: application/json' \
-d '{
    "sepal_length":2.5,
    "sepal_width":1.5,
    "petal_length":4.5,
    "petal_width":0.5
}'
```

*** this project was inspired by and derives from an ungraded lab in this Coursera course: [Deploying Machine Learning Models in Production](https://www.coursera.org/learn/deploying-machine-learning-models-in-production).  

