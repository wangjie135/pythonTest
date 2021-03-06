#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

import pycurl

c = pycurl.Curl()
c.setopt(c.URL, 'http://pycurl.sourceforge.net/tests/testfileupload.php')

c.setopt(c.HTTPPOST, [
    ('fileupload', (
        # upload the contents of this file
        c.FORM_FILE, __file__,
    )),
])

c.perform()
c.close()
