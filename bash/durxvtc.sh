#!/usr/bin/env sh

if [[ -z $(ps -A|grep urxvtd) ]]; then
    urxvtd & 
    sleep 1
    echo "urxvtd launched"
fi

exec urxvtc

exit 0

