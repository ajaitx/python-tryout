#!/usr/bin/python

import os

def push_to_file(fname, data, mode="w"):
        fh = open(fname, mode);
        ret = fh.write(data);
        fh.close();
        return ret;

def pop_from_file(fname, mode="r", line=0):
        fh = open(fname, mode);
        if line :
                fdata = fh.readlines()[line - 1];
        else:
                fdata = fh.read();
        fh.close();
        return fdata;

def dump_file(fname):
        fh = open(fname, 'rb');
        with fh as file:
                for byte in iter(lambda: file.read(1), b''):
                        print (byte);
        fh.close();
        return 0;
