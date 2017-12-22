# coding = utf8
import imp
import sys

print sys.argv[1]

fp, pathname, description = imp.find_module("index")

try:
    m = imp.load_module("index", fp, pathname, description)
    m.main()
finally:
    if fp:
        fp.close()

