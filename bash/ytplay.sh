#!/usr/bin/env bash

#default prints the first page
page=1

# The default action is to show
buf() {
    show
}

if [[ -z $1 ]]; then
    cat <<< "Usage:
    ytplay.sh \"Video name\" [page [number]]

    ytplay will query the search page of youtube with the video name and format the output by two ways :

    . with nothing but the name of the video it will print the numeroted entire list of the results for the first page
    . the page can also be specified
    . with a number it will display only the url of the video, so you can reuse it easily, for example with a player or youtube-dl

    EXAMPLES OF USE:

    ytplay.sh \"asdf movie\"					   # Will recense the list of the asdf movies
    vlc $\(ytplay.sh \"Atom Heart Mother\" 2 1\)   # Will play Atom Heart Mother with vlc
    "
    exit

fi

if [[ -n $2 ]]; then
    page=$2
fi


if [[ -n $3 ]]; then
    nb=$3
    buf() { play ${nb}; }
fi


# Prints all the numeroted results
show() {
    local i
    local n
    while read i; do
        let n++;
        echo -e "$n $i"
    done
}

# Prints the url of the selected video
play() {
    local i
    local n
    while read i; do
        let n++; 
        if [[ "$n" == "$1" ]]; then 
            echo "$i" | cut -d ' ' -f 1
            break
        fi
    done
}


main() {
    query="https://www.youtube.com/results?search_query=$(echo $1|sed "y/\ /+/")&page=$2"
    wget -q $query -O - |
    sed -rn "s/^.*href=\"(\/watch\?v=[^\"]+)\"[^>]*>([^<]+).*/https:\/\/www.youtube.com\1 - \2/p" | 
    buf
}

main "$1" "${page}"

