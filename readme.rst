This project has been made by Subrata Sarkar(<subrotosarkar32@gmail.com>) ,Sangramjit Chakroborty(<sangramjich@gmail.com>)
1>Place 'VCforPyton27.msi' , visual c++ redistibutable setup and extracted swigwin-3.0.8 in this folder.
   for VCForpython check 'https://www.microsoft.com/en-in/download/details.aspx?id=44266'
   for Visual c++ redistributable setup check 'https://www.microsoft.com/en-in/download/details.aspx?id=29'
   for swigwin-3.0.8 check folder and extract

Add this to environment variable(;C:\Program Files\Common Files\Microsoft\Visual C++ for Python\9.0\VC\bin)[the place where vc for python is installed in your pc]

To run the python file extra packages are needed to be installed along with python.They are:
•	P.I.L or Pillow 
•	Pyaudio 0.2.9[Check http://people.csail.mit.edu/hubert/pyaudio/ for compatibility issues]
•	Pocketsphinx 0.0.9: Helps in speech recognition when online/offline.
•	Pyttsx 1.1: Performs text to speech using service on OS.
•	Enchant 1.6: Helps in performing spell-check.
•	pyhinavrophonetic 1.0.0: Helps in phonetic conversion of English to hindi
•	pyhinengphonetic 1.0.0: Helps in conversion of hindi to English text to be spoken using pyttsx
•	speech_recognition 3.4.2: Helps in speech recognition by providing interface for accessing various speech recognition services
•	PyQt 4 4.11.4: Here used for providing print preview window and printing purpose.
•	pywin32: for setting file icons etc on windows

After installing pyenchant copy 'hi_IN.dic' to '\Python\Lib\site-packages\enchant\share\enchant\myspell'
To Install PyAudio 0.2.9\(any *.whl file)
1> go to cmd type:'python -m pip install pyaudio'
     If does not work;
       Install nightly wheel(.whl)
      download it from PyPI
      go to cmd type:'python -m pip install %%name of file downloded(full pathname)%%'
     else,
       download it from PyPI
       extract the *.tar.gz
       open cmd and go to respective folder
       type command:'python setup.py build'
                                  'python setup.py install'
Install Speech Recognition 3.4.3-3.4.6
download it from PyPI
extract the file(for files compressed as *.tar.gz)
open cmd and go to respective folder
type command:'python setup.py build'
             'python setup.py install'

You need PyAudio 0.2.9+ for speech recognition.
For using sphinx you need to download hindi language model and set sphinxbase on your pc
Thenby running 'enigmapad.py'.

P.S.:After installing pyhinavrophonetic and pyhinengphonetic go to the directory where python is installed the go'\Lib\site-packages' and open the folders 'pyhinavrophonetic-1.0.0-py2.7.egg' & 'pyhinengphonetic-1.0.0-py2.7.egg' and copy paste the folders 'pyhinavrophonetic' and 'pyhinengphonetic' from them to site packages check pocketsphinx for the same. Install pocketsphinx after installing 'VCForPython27 .msi' and setting system variable by running the file 'EnigmaPad\changepathspeech.py'.

You might feel irritatd if you wished to use the software not explore it then you can visit 'https://pagamesltd.blogspot.in/p/enigmapad.html'.
