#!/usr/bin/env python2

import sys
import fileinput
import markdown

markdown.markdownFromFile(input=sys.argv[1],
                          output="test.html",
                          encoding="utf8")
