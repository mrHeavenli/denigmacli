#!/bin/python3
import requests
import sys
import json

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

def parse_code_file(path):
    form_dict = {}
    with open(path) as file:
        for line in file.readlines():
            form_dict[line] = ""
    return form_dict

form_data = parse_code_file(sys.argv[1])

req = requests.request("POST", "https://service.denigma.app/explain/demo/?p=1&engine_version=1", data=form_data, headers=headers)

for line in json.loads(req.text)["data"]:
    print(line)