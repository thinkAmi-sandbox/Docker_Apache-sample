#!/usr/bin/python3
# coding: utf-8
from mod_python import apache

def handler(req):
    req.content_type = 'text/plain'
    req.write("Hello World!")
    return apache.OK