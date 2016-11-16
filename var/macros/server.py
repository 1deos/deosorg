#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
web.config.debug = False
urls = ('/', 'index')
class index:
    def GET(self):
        return 'yo, world!'
app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()
