# IPython log file

import subprocess as s
import json


mydict = dict(
    one='foo',
    two='bar',
    three='baz')


d = json.dumps(mydict)
d = d.encode('utf-8')


out = s.check_output("jq '.'", input=d, shell=True)


out = out.decode('utf-8')
out = out.replace('\n','')


