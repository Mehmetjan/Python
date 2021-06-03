import json
import re
x= '{"name": "mehmet",  "age": 31, "career": "marketing" }'

y = json.loads(x)
print(y["age"])




txt = "The rain in Spain"
x1 = re.search("^The.*Spain$", txt)
print(x1)