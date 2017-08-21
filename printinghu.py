# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtCore, QtGui
from httpWidget import Ui_Form as Ui_HttpWidget

class httpWidget(QtGui.QWidget):
    def __init__(self, parent=None,url=''):
        super(httpWidget, self).__init__(parent)
        self.ui = Ui_HttpWidget()
        self.ui.setupUi(self)
        
        # set margins

        self.ui.horizontalLayout.setMargin(5)
        
        # set the default page
        self.ui.url.setText(url)
        
        # load page
        self.ui.webView.setUrl(QtCore.QUrl(url))
        
        # history buttons:
        self.ui.back.setEnabled(False)
        self.ui.next.setEnabled(False)
        
        QtCore.QObject.connect(self.ui.back,QtCore.SIGNAL("clicked()"), self.back)
        QtCore.QObject.connect(self.ui.next,QtCore.SIGNAL("clicked()"), self.next)
        QtCore.QObject.connect(self.ui.url,QtCore.SIGNAL("returnPressed()"), self.url_changed)
        QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("linkClicked (const QUrl&)"), self.link_clicked)
        QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("urlChanged (const QUrl&)"), self.link_clicked)
        QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("loadProgress (int)"), self.load_progress)
        QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&)"), self.title_changed)
        QtCore.QObject.connect(self.ui.reload,QtCore.SIGNAL("clicked()"), self.reload_page)
        QtCore.QObject.connect(self.ui.stop,QtCore.SIGNAL("clicked()"), self.stop_page)
        QtCore.QObject.connect(self.ui.printi,QtCore.SIGNAL("clicked()"), self.homepage)
        QtCore.QObject.connect(self.ui.printp,QtCore.SIGNAL("clicked()"), self.preview)
        
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def url_changed(self):
        """
        Url have been changed by user
        """
        page = self.ui.webView.page()
        history = page.history()
        if history.canGoBack():
            self.ui.back.setEnabled(True)
        else:
            self.ui.back.setEnabled(False)
        if history.canGoForward():
            self.ui.next.setEnabled(True)
        else:
            self.ui.next.setEnabled(False)
        
        url = self.ui.url.text()
        self.ui.webView.setUrl(QtCore.QUrl(url))
        
    def stop_page(self):
        """
        Stop loading the page
        """
        self.ui.webView.stop()
    
    def title_changed(self, title):
        """
        Web page title changed - change the tab name
        """
        self.setWindowTitle(title)
    
    def reload_page(self):
        """
        Reload the web page
        """
        self.ui.webView.setUrl(QtCore.QUrl(self.ui.url.text()))
    
    def link_clicked(self, url):
        """
        Update the URL if a link on a web page is clicked
        """
        page = self.ui.webView.page()
        history = page.history()
        if history.canGoBack():
            self.ui.back.setEnabled(True)
        else:
            self.ui.back.setEnabled(False)
        if history.canGoForward():
            self.ui.next.setEnabled(True)
        else:
            self.ui.next.setEnabled(False)
        
        self.ui.url.setText(url.toString())
    
    def load_progress(self, load):
        """
        Page load progress
        """
        if load == 100:
            self.ui.stop.setEnabled(False)
        else:
            self.ui.stop.setEnabled(True)
        
    def back(self):
        """
        Back button clicked, go one page back
        """
        page = self.ui.webView.page()
        history = page.history()
        history.back()
        if history.canGoBack():
            self.ui.back.setEnabled(True)
        else:
            self.ui.back.setEnabled(False)
    
    def next(self):
        """
        Next button clicked, go to next page
        """
        page = self.ui.webView.page()
        history = page.history()
        history.forward()
        if history.canGoForward():
            self.ui.next.setEnabled(True)
        else:
            self.ui.next.setEnabled(False)

    def preview(self):

                # Open preview dialog
                preview = QtGui.QPrintPreviewDialog()
                # If a print is requested, open print dialog
                preview.paintRequested.connect(lambda p: self.ui.webView.print_(p))

                preview.exec_()

    def homepage(self):

        self.ui.url.setText('http://pagamesltd.blogspot.in/')
        self.url_changed()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = httpWidget(url='http://google.com')
    myapp.show()
    app_icon = QtGui.QIcon()
    app_icon.addFile('data/banglakey1.ico', QtCore.QSize(16,16))
    app_icon.addFile('data/banglakey12.ico', QtCore.QSize(32,32))
    app_icon.addFile('data/banglakey13.ico', QtCore.QSize(48,48))
    app.setWindowIcon(app_icon)
    sys.exit(app.exec_())
def call(fname):
    app = QtGui.QApplication(sys.argv)
    myapp = httpWidget(url=fname)
    myapp.show()
    app_icon = QtGui.QIcon()
    app_icon.addFile('data/banglakey1.ico', QtCore.QSize(16,16))
    app_icon.addFile('data/banglakey12.ico', QtCore.QSize(32,32))
    app_icon.addFile('data/banglakey13.ico', QtCore.QSize(48,48))
    app.setWindowIcon(app_icon)
    app.exec_()
