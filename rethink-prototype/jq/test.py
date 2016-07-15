# use jq output as variable

import subprocess as s
import sys
import json
import logging
from traceback import format_exc


logger = logging.getLogger('example')
logging.basicConfig(level=logging.DEBUG)


d = dict(
        one = 'foo',
        two = 'bar',
        three = 'baz',
        four = 'spam')

d = json.dumps(d)





