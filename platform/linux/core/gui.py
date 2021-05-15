#!/usr/bin/env python3 
# -*- coding: utf-8 -*-"

"""
- Code by: Keany Vy KHUN
- Name: lemonrouter
- Organization: Decentralize Me
- Version: 1.0
"""

import sys, os
from lookup import *
from PyQt5.QtWidgets import * 
from PyQt5 import QtNetwork, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

#verify if this is a linux
def verifySys():
    #linux system
    if sys.platform == "linux" or sys.platform == "linux2":
        app.exec_()
    #macos system
    elif sys.platform == "darwin":
        print(GREEN + """
    Mac Os detected, you need to use linux...
        """)
        exit()
    #windows system
    elif sys.platform == "win32" or sys.platform == "win64":
        print(GREEN + """
    Windows detected, you need to use linux...
        """)
        exit()
    #other system
    else:
        print(GREEN + """
    Unable to identify operating system...
        """)
        exit()

#connect to tor proxy

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('assets/favicon.svg')) #change the path
        self.label = QLabel("Lemon Router", self)
        self.label.move(100, 100)
        self.show()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        #btn1
        back_btn = QAction('Return', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        #btn2
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        #btn3
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        #btn4
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        #btn5
        dom_btn = QAction('Dom', self)
        dom_btn.triggered.connect(self.website)
        navbar.addAction(dom_btn)
        #btn5
        ip_btn = QAction(ip, self)
        ip_btn.triggered.connect(self.my_ip)
        navbar.addAction(ip_btn)
        #url bar to navigate
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        #change url
        self.browser.urlChanged.connect(self.update_url)

    def my_ip(self):
        self.browser.setUrl(QUrl('https://location.ipfire.org/'))

    def website(self):
        self.browser.setUrl(QUrl('https://github.com/decentralizeme'))

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if "https://" in url or "http://" in url:
            self.browser.setUrl(QUrl(url))
        else:
            validurl = url.split(".")
            if len(validurl) > 1:
                if " " not in url:
                    newsecureurl = f"https://{url}"
                    self.browser.setUrl(QUrl(newsecureurl))
                else:
                    self.browser.setUrl(QUrl("https://duckduckgo.com/?q="+url))
            else:
                self.browser.setUrl(QUrl("https://duckduckgo.com/?q="+url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

#conf
app = QApplication(sys.argv)
QApplication.setApplicationName('Lemon Router')
window = MainWindow()

if __name__ == "__main__":
    verifySys() #first function