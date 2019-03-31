#!/usr/bin/env bash

usage () {
    echo
    echo "Use: ./run.sh [dev|prod]"
    echo
}

if [ "$#" == 0 -o "$1" == "-h" -o "$1" == "--help" ]
then
    echo
    echo "Startup script application."
    usage
    exit 1
fi

case "$1" in
    dev)
        export DEBUG=True
        python3 manage.py runserver 0:8000
        ;;
    prod)
        export DEBUG=False
        if [ -z "$DATABASE_URL" ]
        then
            # Default database, set the real string connection from the environment
            # variable instead of hardcoding here
            export DATABASE_URL="postgresql://dmysite:postgres@localhost/dmysite_dev"
        fi
        echo -n "Starting uWSGI server for Django mysite... "
        uwsgi --module=mysite.wsgi:application \
              --master --pidfile=/tmp/dmysite-master.pid \
              --http=127.0.0.1:8000 \
              --processes=5 \
              --max-requests=5000 \
              --vacuum \
              --daemonize=dmysite.log
        sleep 0.7
        echo "started with PID $(cat /tmp/dmysite-master.pid)"
        ;;
    *)
        echo
        echo "./run ERROR: unknown '$1' environment."
        echo
        usage
        exit 2
        ;;
esac
