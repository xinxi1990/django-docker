introduction
=============
this project have three api to test

1、http://0.0.0.0:8000/polls/add

2、http://0.0.0.0:8000/polls/del

3、http://0.0.0.0:8000/polls/update


venv
=============

venv use isolation environment

pip install virtualenv

virtualenv venv

virtualenv -p /usr/bin/python2.7 venv　

source venv/bin/activate

python2.7 manage.py runserver 0.0.0.0:8000

deactivate

mysql
=============

```
docker run --name some-mysql -v /root/qamysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123321 -p 8888:3306 -d mysql:5.5
```

already create db(android) table(t_android)


postman to test
=============
postman folder have django_test.postman_collection.json

you can import local postman to test


debug
=============
```
python2.7 manage.py runserver 0.0.0.0:8000
```


online
=============
```
gunicorn -c gunicorn.conf.py  wsgi:application -D
```



django-docker
=============

Demo Django App using Docker


Dockerfile
----------
Use this to build a new image

    $ sudo docker build .

With a tag for easier reuse

    $ sudo docker build  -t <your username>/django-docker .

Running the container

    $ sudo docker run -d -p :8000 <your username>/django-docker
    
Get your container's IP Address:

    sudo docker inspect <container_id> | grep IPAddress | cut -d '"' -f 4

Now go to `<your container's ip>:8000` in your browser