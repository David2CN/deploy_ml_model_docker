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
-d '{ "batches": [
    [
        0.5,
        0.1,
        1.2,
        2.4
    ]
]
}'
```
The list in the curl command above should follow this ordering: <br>
[sepal_length, sepal_width, petal_length, petal_width]

*** this project was inspired by and derives from an ungraded lab in this Coursera course: [Deploying Machine Learning Models in Production](https://www.coursera.org/learn/deploying-machine-learning-models-in-production).  

