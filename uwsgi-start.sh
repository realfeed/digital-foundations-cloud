#!/bin/bash

cd /var/app
. bin/activate
uwsgi --http :8080 --chdir /var/app --wsgi-file plotter.py --callable app --master --processes $UWSGI_NUM_PROCESSES --threads $UWSGI_NUM_THREADS --enable-threads --uid $UWSGI_UID --gid $UWSGI_GID #--logto2 $UWSGI_LOG_FILE
