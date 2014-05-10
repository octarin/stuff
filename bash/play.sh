#!/usr/bin/env bash

if [[ -z $2 ]]; then
    nb=1
else
    nb=$2
fi

vlc $(curl -s www.youtube.com/results?search_query=$1|sed -rn "s/.*href=\"(\/watch\?v=[^\"]+)\".*/http:\/\/www.youtube.com\1/p"|head -n $nb)
