import os
def load_file(file):# function to load images
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file1 = os.path.join(main_dir)        
        return file1

def write_registry():
    import os.path
    import _winreg as winreg
    k=''
    file2=load_file('changepathspeech.py')

    file2+='\\'
    k+=file2
    k.replace('/','\\')
    
    gpxkey1 = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, '.egpd')
    winreg.SetValue(gpxkey1, None, winreg.REG_SZ, 'EnigmaPad file') # what was needed!
    winreg.CloseKey(gpxkey1)
    gpxkey = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'EnigmaPad')
    winreg.SetValue(gpxkey, None, winreg.REG_SZ, 'EnigmaPad') # what was needed!
    iconkey = winreg.CreateKey(gpxkey, 'DefaultIcon')
    winreg.SetValue(iconkey, None, winreg.REG_SZ, k+r'data\enigmapad.ico')    
    winreg.CloseKey(iconkey)
    openkey = winreg.CreateKey(gpxkey, 'shell\\open\\command')
    winreg.SetValue(openkey, None, winreg.REG_SZ,'""'+k+'EnigmaPad.exe"" ""%1""' )    
    winreg.CloseKey(openkey)
    winreg.CloseKey(gpxkey)
    
write_registry()
