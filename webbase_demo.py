#encoding:utf-8
import htmlPy

web_app = htmlPy.WebAppGUI(title=u"Python Website", maximized=True)
web_app.url = u"http://www.zhihu.com/"

web_app.start()