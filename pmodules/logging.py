#!/usr/bin/python

import __builtin__
from fileops import *

# Global variables 
__builtin__.glogLevel = 0;
__builtin__.glogLocalPrint = 0;
__builtin__.glogSyslog = 0;

# To set global configuration of logging
def set_global_log_conf(level, localFlag, syslogFlag):
    __builtin__.glogLevel = level;
    __builtin__.glogLocalPrint = localFlag;
    __builtin__.glogSyslog = syslogFlag;


# Custom printf function
def dPrintf(level, data):
    if level <= glogLevel:
        if glogLocalPrint == 1 :
            print data;
        if glogSyslog == 1 :
            push_to_file("app.log", data);
