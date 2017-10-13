#!/usr/bin/python

from fileops import *
from logging import *

# set logging global config
set_global_log_conf(1,1,1);

#File operations 
push_to_file("sample.txt", "Hello world1", "w");
push_to_file("sample.txt", "\nHello world2", "a");
dump_file("sample.txt");

#Custom print usage
dPrintf(0, "Sample loging");
