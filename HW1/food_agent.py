#!/usr/bin/python
#Andres Chorro, Jannette Pham-Le, Justin Tieu
def readTextFile():
	f = open("map.txt")
	line = f.read()
	while line:
	   print line, #comma omits print's newline char
	   line = f.read()
	f.close()

readTextFile();
