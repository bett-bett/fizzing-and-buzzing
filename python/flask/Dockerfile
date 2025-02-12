# Stage 1: base
FROM python:3.10-slim as base
WORKDIR /fizzbuzz-app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final 
FROM base as final
WORKDIR /fizzbuzz-app
COPY . . 

ENV FLASK_APP=fizzbuzz-app
ENV FLASK_RUN_PORT=5002
ENV FLASK_ENV=development

EXPOSE 5002

CMD ["flask", "run", "--host=0.0.0.0"]

# podman build -t flask-fizz .
# podman run -p 5000:5002 flask-fizz

# "Yeah Buoiyy"
# now remove that container coz I know you wll forget and wonder where all the sweet Gigabytes went
# podman ps -a                        # List all containers
# podman stop <container_id>          # Stop the container
# podman rm <container_id>            # Remove the container
# podman images                       # List all images
# podman rmi <image_id>               # Remove the image
# podman volume prune                 # Remove unused volumes


# honestly, I just use lazydocker.

