#!/usr/bin/python

from fileops import *

push_to_file("sample.txt", "Hello world1", "w");
push_to_file("sample.txt", "\nHello world2", "a");
dump_file("sample.txt");

