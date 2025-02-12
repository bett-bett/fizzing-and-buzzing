## run flask app
```
flask run
```

http://127.0.0.1:5002/


## using docker
```
podman build -t flask-fizzbuzz .
podman run -p 5000:5002 flask-fizzbuzz
```
