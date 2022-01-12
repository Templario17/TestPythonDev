#!/usr/bin/env python3
from os.path import isfile
import json

from settings import MODULE_PATH, PACKAGE, CONTROLLER, RESOURCE, HTTP_404,\
    HTTP_HTML, SHOW_ERROR_404, HTTP_REDIRECT, MODULE, API, HOST


error_module = error_resource = True

if isfile(MODULE_PATH):
    modulo = __import__(PACKAGE, fromlist=[CONTROLLER])
    controller = getattr(modulo, CONTROLLER)(API)
    error_module = False

if not error_module and hasattr(controller, RESOURCE):
    getattr(controller, RESOURCE)()
    error_resource = False

if error_module or error_resource:
    print("Content-type: application/json; charset=utf-8")
    print("Access-Control-Allow-Origin: *")
    print("")
    response = {"msg": 'not Found', 'status': '404'}
    print(json.dumps(response))
