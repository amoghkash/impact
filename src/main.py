import random
import data.input as input
import data.processing as processing
import logger.logger as logger
import time
#import plot as visualizer
import variable.const as constant
import simpleaudio 
import tkinter as tk



starttime = time.time()
wave_obj = simpleaudio.WaveObject.from_wave_file("beep.wav")


root = tk.Tk()
root.title("Player Monitoring Service")


player1 = tk.Label(root, text="placeholder", borderwidth=2, relief="solid", font=('Helvetica', 50))
player1.grid(column=0, row=1, padx=50, pady=10)



print('\a')



def set_label():
    rawdata = input.getdata()
    data = processing.normalize(rawdata)
    magnitudevalue = float(processing.getmagnitude(data))
    data.append(magnitudevalue)
    timestamp = time.time() - starttime
    data.append(timestamp)
    print(data)
    logger.log(data, constant.datafile)
    if(magnitudevalue>30):
        x=0
        print("Impact Detected")
        player1['bg'] = "red"
        play_obj = wave_obj.play()



    data1 = magnitudevalue
    #data1 = random.uniform(5.85,50.93)
    player1['text'] = "Player 1: " + str(round(data1, 2))
    root.after(1, set_label)
    


set_label()
root.mainloop()

    
