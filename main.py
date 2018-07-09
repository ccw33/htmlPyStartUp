#encoding:utf-8
import htmlPy
import os

import htmlPy
from back_end import BackEnd

app = htmlPy.AppGUI(title=u"htmlPy Quickstart", maximized=True,developer_mode=True)

app.template_path = os.path.abspath("template")
app.static_path = os.path.abspath("static")

#绑定后台
app.bind(BackEnd(app))

app.template = ("index.html", {"username": "htmlPy_user"})

if __name__=="__main__":
    app.start()