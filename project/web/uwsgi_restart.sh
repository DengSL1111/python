ps -ef | grep uwsgi | grep -v grep | awk '{print $2}' | xargs kill -9

echo 'stop uwsgi....'
sleep 1
ps -aux | grep uwsgi

echo 'start uwsgi....'
uwsgi -x /data/website/mysite/mysite.xml
ps -aux | grep uwsgi

/etc/init.d/nginx restart

