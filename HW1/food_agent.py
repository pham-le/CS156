#!/usr/bin/python

def readTextFile():
	f = open("map.txt")
	line = f.read()
	while line:
	   print line, #comma omits print's newline char
	   line = f.read()
	f.close()

readTextFile();
