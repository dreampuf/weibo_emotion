#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-

from __future__ import with_statement
import sys
import urllib2
from contextlib import closing

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        from django.utils import simplejson as json

with open("positive.txt") as f:
    po_corpus = [i.decode("u8") for i in f.xreadlines()]

with open("negative.txt") as f:
    ne_corpus = [i.decode("u8") for i in f.xreadlines()]

def main(uid):
    ret = None
    with closing(urllib2.urlopen("%s%s" % ("http://v.t.sina.com.cn/widget/getusermblog.php?uid=", uid))) as f:
        ret = json.load(f)
    
    if ret is None:
        raise RuntimeError("Bad uid")

    usr_txt = [i["content"]["text"] for i in ret["result"]]
    po = ne = 0
    po = sum(map(lambda x: len(filter(lambda word: word in x, po_corpus)), usr_txt))
    ne = sum(map(lambda x: len(filter(lambda word: word in x, ne_corpus)), usr_txt))

    print "Positive:%s\nNegative:%s" % (po, ne)

if __name__ == "__main__":
    main(sys.argv[1])

