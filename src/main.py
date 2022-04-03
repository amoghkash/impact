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

player2 = tk.Label(root, text="placeholder", borderwidth=2, relief="solid", font=('Helvetica', 50))
player2.grid(column=0, row=2, padx=50, pady=10)

player3 = tk.Label(root, text="placeholder", borderwidth=2, relief="solid", font=('Helvetica', 50))
player3.grid(column=0, row=3, padx=50, pady=10)

player4 = tk.Label(root, text="placeholder", borderwidth=2, relief="solid", font=('Helvetica', 50))
player4.grid(column=1, row=1, padx=50, pady=10)

player5 = tk.Label(root, text="placeholder", borderwidth=2, relief="solid", font=('Helvetica', 50))
player5.grid(column=1, row=2, padx=50, pady=10)

player6 = tk.Label(root, text="placeholder", borderwidth=2, relief="solid", font=('Helvetica', 50))
player6.grid(column=1, row=3, padx=50, pady=10)

player7 = tk.Label(root, text="placeholder", borderwidth=2, relief="solid", font=('Helvetica', 50))
player7.grid(column=3, row=1, padx=50, pady=10)

player8 = tk.Label(root, text="placeholder", borderwidth=2, relief="solid", font=('Helvetica', 50))
player8.grid(column=3, row=2, padx=50, pady=10)

player9 = tk.Label(root, text="placeholder", borderwidth=2, relief="solid", font=('Helvetica', 50))
player9.grid(column=3, row=3, padx=50, pady=10)

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
    data2 = random.uniform(5.85,50.93)
    data3 = random.uniform(5.85,50.93)
    data4 = random.uniform(5.85,50.93)
    data5 = random.uniform(5.85,50.93)
    data6 = random.uniform(5.85,50.93)
    data7 = random.uniform(5.85,50.93)
    data8 = random.uniform(5.85,50.93)
    data9 = random.uniform(5.85,50.93)
    player1['text'] = "Player 1: " + str(round(data1, 2))
    player2['text'] = "Player 2: " + str(round(data2, 2))
    player3['text'] = "Player 3: " + str(round(data3, 2))
    player4['text'] = "Player 4: " + str(round(data4, 2))
    player5['text'] = "Player 5: " + str(round(data5, 2))
    player6['text'] = "Player 6: " + str(round(data6, 2))
    player7['text'] = "Player 7: " + str(round(data7, 2))
    player8['text'] = "Player 8: " + str(round(data8, 2))
    player9['text'] = "Player 9: " + str(round(data9, 2))
    root.after(1, set_label)
    


set_label()
root.mainloop()

    
