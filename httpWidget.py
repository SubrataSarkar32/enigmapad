# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'httpWidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtWebKit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.reload = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.reload.setObjectName(_fromUtf8("reload"))
        self.horizontalLayout.addWidget(self.reload)
        self.next = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.next.setObjectName(_fromUtf8("next"))
        self.horizontalLayout.addWidget(self.next)
        self.back = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.back.setObjectName(_fromUtf8("back"))
        self.horizontalLayout.addWidget(self.back)
        self.stop = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.horizontalLayout.addWidget(self.stop)
        self.webView = QtWebKit.QWebView(Form)
        self.webView.setGeometry(QtCore.QRect(10, 100, 780, 490))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.url = QtGui.QLineEdit(Form)
        self.url.setGeometry(QtCore.QRect(10, 60, 621, 31))
        self.url.setObjectName(_fromUtf8("url"))
        self.printi = QtGui.QPushButton(Form)
        self.printi.setGeometry(QtCore.QRect(630, 17, 50, 25))
        self.printi.setObjectName(_fromUtf8("print"))
        self.printp = QtGui.QPushButton(Form)
        self.printp.setGeometry(QtCore.QRect(635, 60, 80, 30))
        self.printp.setObjectName(_fromUtf8("printpreview"))
        
         
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.reload.setText(_translate("Form", "Reload", None))
        self.next.setText(_translate("Form", "Next", None))
        self.back.setText(_translate("Form", "Back", None))
        self.stop.setText(_translate("Form", "Stop", None))
        self.printi.setText(_translate("Form", "Home", None))
        self.printp.setText(_translate("Form", "Print Preview", None))
        

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    app_icon = QtGui.QIcon()
    app_icon.addFile('data/banglakey1.ico', QtCore.QSize(16,16))
    app_icon.addFile('data/banglakey12.ico', QtCore.QSize(32,32))
    app_icon.addFile('data/banglakey13.ico', QtCore.QSize(48,48))
    app.setWindowIcon(app_icon)
    Form.show()
    sys.exit(app.exec_())

