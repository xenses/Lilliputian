#!/usr/bin/env python2

import sys
import markdown
import time
from datetime import date

filename = str(date.today())

markdown.markdownFromFile(input=sys.argv[1],
                          output="/home/laura/public_html/blog/" + filename + ".html",
                          encoding="utf8")

