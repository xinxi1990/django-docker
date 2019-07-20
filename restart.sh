#!/bin/sh

echo "----------------------- 开始启动应用-----------------------"

gun_id=`ps -ef | grep gunicorn | grep -v "grep" | awk '{print $2}'`
echo $gun_id

for id in $gun_id
do
    kill -9 $id
    echo "killed $id"
done

nohup gunicorn -c gunicorn.conf.py  wsgi:application -D &

echo "----------------------- 应用启动完成 -----------------------"

