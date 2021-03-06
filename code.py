import web
import os
from web import form
from time import localtime


web.config.debug = True


urls = (
    '/', 'index',
    '/add', 'add',
    '/checkbox', 'checkbox',
    '/reset', 'reset',
    '/prioritize', 'prioritize'
)


test_environments = ('', 'qa', 'stg', 'prod')
#db_dir = "\\\\shenas01\\qa\\qtp new\\data\\"
db_dir = "c://MyPy//qtprunner//static//"
render = web.template.render('c://MyPy//qtprunner//templates//')
db = web.database(dbn='sqlite', db = db_dir + 'test.db')


application = web.application(urls, globals()).wsgifunc()


class index:
    def GET(self):
        actions = db.select('actions', order="priority")
        return render.index(actions)
    

class checkbox:
    def POST(self):
        to_run = web.input(to_run=[])
        ls = to_run.items()
        test_env = ls[0][1]
        #schedule_task = "cscript.exe c:\\MyPy\\qtprunner\\scripts\\schedule_%s.vbs" %(test_environments[int(test_env)])
        checks = ls[1][1]
        whereclause = 'actionid in (' + ','.join(checks) + ')'
        db.update('actions', where=whereclause, Torun = test_env)
        #os.system(schedule_task)
        raise web.seeother('/')


class reset:
    def POST(self):
        db.update('actions', where="1 = 1",  Torun = 0, status=None)
        raise web.seeother('/reset')

    def GET(self):
        actions = db.select('actions', order="priority")
        return render.reset(actions)


class add:
    def POST(self):
        i = web.input()
        action_priority = int(i.action_priority) + 1 #next priority
        n = db.insert('actions', action_name = i.action_name, action_loc = i.action_loc, priority = action_priority, Torun = 0)
        raise web.seeother('/')


class prioritize:
    def POST(self):
        i = web.input()
        raise web.seeother('/')
    

    def GET(self):
        actions = db.select('actions', order="priority")
        return render.prioritize(actions)
