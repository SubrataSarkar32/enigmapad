from _winreg import *
import os, sys, win32gui, win32con

k=r'C:\Program Files\Common Files\Microsoft\Visual C++ for Python\9.0\VC\bin;'

print k
import os.path
def load_file(file):# function to load images
        '''This function returns original image if PIL is present else runs not avaible image'''
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file1 = os.path.join(main_dir, 'swigwin-3.0.8')        
        return file1
file2=load_file('changepathspeech.pyc')

file2+='\\'
k+=file2
file2.replace('/','\\')
k.replace('/','\\')
os.environ["PATH"] += os.pathsep + file2
print k
def queryValue(key, name):       
    value, type_id = QueryValueEx(key, name)
    return value

def show(key):
    for i in range(1024):                                           
        try:
            n,v,t = EnumValue(key, i)
            print '%s=%s' % (n, v)
        except EnvironmentError:
            break          
def main2(k=''):
    if k!='':
        try:
            path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
            reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
            key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)
            
            if k=='Path':
                show(key)
            else:
                name, value = sys.argv[1].split('=')
                if name.upper() == 'PATH':
                    value = queryValue(key, name) + ';' + value
                if value:
                    SetValueEx(key, name, 0, REG_EXPAND_SZ, value)
                else:
                    DeleteValue(key, name)
                
            win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
                                
        except Exception, e:
            print e
def main(k=''):
    if k!='':
        try:
            path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
            reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
            key = OpenKey(reg, path, 0, KEY_ALL_ACCESS)
            
            if len(sys.argv) == 1:
                show(key)
            else:
                name, value = sys.argv[1].split('=')
                if name.upper() == 'PATH':
                    value = queryValue(key, name) + ';' + value
                if value:
                    SetValueEx(key, name, 0, REG_EXPAND_SZ, value)
                else:
                    DeleteValue(key, name)
                
            win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
                                
        except Exception, e:
            print e

    CloseKey(key)    
    CloseKey(reg)


    
'''if __name__=='__main__':
    
    usage = \
"""
Usage:

Show all environment vsarisbles - enver
Add/Modify/Delete environment variable - enver <name>=[value]

If <name> is PATH enver will append the value prefixed with ;

If there is no value enver will delete the <name> environment variable

Note that the current command window will not be affected, 
only new command windows.
"""
    argc = len(sys.argv)
    if argc > 2 or (argc == 2 and sys.argv[1].find('=') == -1):
        print usage
        sys.exit()
        
    main() '''   
