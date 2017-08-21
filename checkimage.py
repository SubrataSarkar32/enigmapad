def load_image(file):# function to load images
        '''This function returns original image if PIL is present else runs not avaible image'''
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, file)        
        try:
             from PIL import ImageTk,Image
             q = ImageTk.PhotoImage(Image.open(file))
             return q
        except ImportError:
             print 'PIL not found.Please install and run'
             q=Tkinter.PhotoImage(file=str(file))
             return q
import Tkinter,os,time
from PIL import ImageTk,Image
game=Tkinter.Tk()#Here the main parent program strats


game.minsize(250,210)
game.maxsize(250,210)
game.geometry('{}x{}+{}+{}'.format(250, 210, 100, 100))
filename='data/enigma.gif'
img0 = load_image('data/enigmapad.PNG')
img0.imageList=[]
game.configure(background='white')
L6 = Tkinter.Label(game, image = img0)
L6.pack(side = Tkinter.TOP,fill = Tkinter.BOTH)
for i in range(17):
        img0.imageList.append(ImageTk.PhotoImage(Image.open('data/enigmapad.PNG')))
j=0
try:
        import pyaudio
        import wave
        import sys

        CHUNK = 1024
        import Tkinter,os,time
        file='data/door_lock.wav'
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, file)        



        wf = wave.open(file, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                  channels=wf.getnchannels(),
                  rate=wf.getframerate(),
                  output=True)
        def cancel():
                global solve
                game.after_cancel(solve)
                solve=None

                

        def update_image():
            global solve
            global wf
            global p
            global j
            if j==117:
                  cancel()
                  game.configure(background='white')
                  L6.configure(background='white')
                  

                  data = wf.readframes(CHUNK)

                  while data != '':
                      stream.write(data)
                      data = wf.readframes(CHUNK)

                  stream.stop_stream()
                  stream.close()

                  p.terminate()          
                  game.destroy()
            elif j<117:
                    if j<17:
                          game.configure(background='white')
                          
                    elif j>=17 or j<96:
                          game.configure(background='black')
                          L6.configure(background='black')
                    elif j>=96:
                          game.configure(background='white')
                          L6.configure(background='white')
                    
                    L6.configure(image=img0.imageList[j])
                    print j
                    j+=1    
                    solve=game.after(1,update_image)
except:
        import sys

        
        import Tkinter,os,time
        file='data/door_lock.wav'
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, file)        
        def cancel():
                global solve
                game.after_cancel(solve)
                solve=None

                

        def update_image():
            global solve
            global j
            if j==117:
                  cancel()
                  game.configure(background='white')
                  L6.configure(background='white')
                  

                      
                  game.destroy()
            elif j<117:
                    if j<17:
                          game.configure(background='white')
                          
                    elif j>=17 or j<96:
                          game.configure(background='black')
                          L6.configure(background='black')
                    elif j>=96:
                          game.configure(background='white')
                          L6.configure(background='white')
                    
                    L6.configure(image=img0.imageList[j])
                    print j
                    j+=1    
                    solve=game.after(1,update_image)

def rotate():
    i=0
    while i<91:
        img01=Image.open('data/enigma.gif')
        img02=img01.rotate(i)
        img0.imageList.append(ImageTk.PhotoImage(img02))
        i+=1
    for i in range(10):
        img0.imageList.append(ImageTk.PhotoImage(Image.open('data/enigmapad1.PNG')))
    update_image()
    
        
solve=None

try:
    k=img0.imageList.pop()
    rotate()   
except IndexError:
    
    rotate()
game.overrideredirect(1)
game.mainloop()
