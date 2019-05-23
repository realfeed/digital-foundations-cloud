FROM       python:3.6

WORKDIR    /var/app

RUN        pip3 install virtualenv
RUN        virtualenv /var/app
RUN        /var/app/bin/pip install --upgrade pip
RUN        /var/app/bin/pip install uwsgi

RUN        useradd uwsgi -s /bin/false
RUN        mkdir /var/log/uwsgi
RUN        chown -R uwsgi:uwsgi /var/log/uwsgi

ADD        ./requirements.txt /var/app
RUN        /var/app/bin/pip install -r /var/app/requirements.txt

ADD        ./app/. /var/app

ENV        UWSGI_NUM_PROCESSES    1
ENV        UWSGI_NUM_THREADS      15
ENV        UWSGI_UID              uwsgi
ENV        UWSGI_GID              uwsgi
ENV        UWSGI_LOG_FILE         /var/log/uwsgi/uwsgi.log

EXPOSE     8080

ADD        uwsgi-start.sh /

CMD        []
ENTRYPOINT ["/uwsgi-start.sh"]
