#!/bin/bash  

if [ $(id -u) != "0" ]; then
        echo "You must be the superuser to run this script." >&2
        exit 1;
fi

usage()
{
cat << EOF
usage: $0 {start|stop|restart}

Starts/Stops/Restarts the following services:
        httpd
        ntpd
EOF
}

if [ $# -ne 2 ]
then
   # echo "myvar equals 3"
usage
fi

process_state() {
/etc/init.d/$1 $2  > /dev/null
}


case "$2" in 
    start)   process_state  $1 $2  ;;
    stop)    process_state $1 $2  ;; 
    restart) process_state $1 $2  ;;
    *) echo "usage: $1 start|stop|restart" >&2
       exit 1
       ;;
esac
