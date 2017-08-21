filen=open('appenreg.txt','r+')
regd=filen.read()
filen.close()
if regd!='1':
   try:
       import write_iconreg
       import os
       os.startfile('vcredist_x86.exe')
       os.startfile('VCForPython27 .msi')
       

       import win32api
       import win32con
       import ctypes

       ctypes.windll.gdi32.AddFontResourceA("Amarbn__.ttf")
       ctypes.windll.gdi32.AddFontResourceA("Siyamrupali.ttf")
       win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_FONTCHANGE)


       import changepathspeech
       
       os.remove('changepathspeech.pyc')
   except Exception as e:
       print e
       print 'Check over!!!'
   filen=open('appenreg.txt','w+')
   filen.write('1')
   filen.close()
   import tkMessageBox
   s=tkMessageBox.askyesno( "Survey", "Would you like to take our survey")
   if s== True:
      import printinghu
      printinghu.call('''https://goo.gl/forms/GCRw1V7iOdNRNg5K2''')
   else:
       pass
del(regd)
