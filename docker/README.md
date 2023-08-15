# Photometry Pipeline Container


- #### Create image: `docker build -t <image-name> .`

- #### Run a container in detached mode with port `9090` exposed: `docker run -d -p 9090:9090 --name <container-name> <image-name>`

- #### Interact with a running container's shell: `docker exec -it <container-id/name> bash`

- #### Test the connection with the http server on `http://localhost:9090/` or `http://127.0.0.1:9090/`

- #### Use `pact` to activate the python environment. 
  
