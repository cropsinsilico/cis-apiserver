# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/api/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/api/v1/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run a RabbitMQ development server in a Docker container:
```bash
docker run --name=rabbitmq -it -d -p 5672:5672 rabbitmq:3.6.2-management
```

To run the apiserver in a Docker container, please execute the following from the root directory:
```bash
# building the image
docker build -t cis-apiserver .

# start up a container
docker run -it -d --name=cis-api -p 8080:8080 --link rabbitmq \
    -e RABBIT_HOST=rabbitmq -e RABBIT_NAMESPACE=apiserver cis-apiserver
```

### Regenerating with Docker

To regenerate the controllers / models via Docker, please execute the following in the root directory:
```bash
docker run -it -v $(pwd):/workspace -w /workspace swaggerapi/swagger-codegen-cli generate -i ./swagger_server/swagger/swagger.yaml -l python-flask -o .
```

This will read the `.swagger-codegen-ignore` file to determine which files should
be overwritten during regeneration. You should see output of which files are
modified as the codegen process executes.

## Testing

You can test the `/simulations` endpoint by sending an HTTP POST to `localhost:8080/v2/simulations`:
```bash
curl -XPOST --header 'Content-Type: application/json' localhost:8080/api/v1/simulations -d '{"models":[{"name":"example:hello_c", "path":"hello/hello_c"}]}'
```

You should see the specified model output in the service logs:
```
[{'name': 'example:hello_c', 'path': 'hello/hello_c'}] <--- array of "Model" objects that will be run
Hello from C
hello(C): Created I/O channels
hello(C): Received 14 bytes from file: this is a test
hello(C): Sent to outq
hello(C): Received 14 bytes from queue: this is a test
hello(C): Sent to outf
Goodbye from C
172.17.0.1 - - [07/Nov/2017 23:49:40] "POST /api/v1/simulations HTTP/1.1" 200 -
INFO:werkzeug:172.17.0.1 - - [07/Nov/2017 23:49:40] "POST /api/v1/simulations HTTP/1.1" 200 -
```
