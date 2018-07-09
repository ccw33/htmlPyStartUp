import json

import htmlPy
class BackEnd(htmlPy.Object):
    def __init__(self, app):
        super(BackEnd, self).__init__()
        self.app = app

    @htmlPy.Slot()
    def say_hello_world(self):
        self.app.html = u"Hello, world"

    @htmlPy.Slot()
    def go_to_demo(self):
        self.app.template = ("demo.html",{})

    @htmlPy.Slot(str,result=str)
    def form_function_name(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.Slot(str,int,result=str)
    def javascript_function(self,name,age):
        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI
        print('hahaha')
        return name+':'+str(age)



    @htmlPy.Slot()
    def python_call_script(self):
        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI
        print('try_demo')
        self.app.evaluate_javascript("call_by_backend('%s')" % json.dumps({'name':'ccw','age':25}))