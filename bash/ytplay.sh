#!/usr/bin/env bash


# The default action is show
buf() {
	show
}

if [[ -z $1 ]]; then
	cat <<< "Usage:
	ytplay.sh \"Video name\" [number]

	ytplay will query the search page of youtube with the video name and format the output by two ways :

	. with nothing but the name of the video it will print the numeroted entire list of the results
	. with a number it will display only the url of the video, so you can reuse it easily, for example with a player or youtube-dl

	EXAMPLES OF USE:

	ytplay.sh \"asdf movie\"                   # Will recense the list of the asdf movies
	vlc $\(ytplay.sh \"Atom Heart Mother\"\) 1 # Will play Atom Heart Mother with vlc
	"

fi



if [[ -n $2 ]]; then
	nb=$2
	buf() { play ${nb}; }
fi


# Prints all the numeroted results
show() {
	while read i; do
		let n++;
		echo -e "$n $i"
	done
}

# Prints the url of the selected video
play() {
	while read i; do
		let n++;
		echo -e "$n $i"|
		{
			if [[ "$n" == "$1" ]]; then 
				cat | cut -d ' ' -f 2
			else 
				cat > /dev/null
			fi
		}
	done
}


curl -s www.youtube.com/results?search_query=$(echo $1|sed "y/\ /+/") | 
sed -rn "s/^.*<h3.*href=\"(\/watch\?v=[^\"]+)\">([^<]+).*/https:\/\/www.youtube.com\1 - \2/p" | 
buf

