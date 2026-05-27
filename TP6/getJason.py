# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: getJason.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-05-06 19:05:36 UTC (1746558336)

import json
import sys

jsonfile = sys.argv[1]

jsonkey = sys.argv[2] if len(sys.argv) > 2 else "token1"

with open(jsonfile, "r") as myfile:
    data = myfile.read()
    
obj = json.loads(data)
print(str(obj[jsonkey]))
