import cv2
import time
import numpy as p
import PySimpleGUI as sg
import subprocess
import logzero
from logzero import logger
from PIL import Image
import glob
import sys
import PIL
from PIL import Image, ImageTk
import os


def main():
    sg.theme('LightBlue4')
    layout_column= [
    [sg.Text("Welcome to Online Assesment" ,justification="centre",size=(40, 1),font=("Helvetica", 25))],
    [sg.Text('_'  * 80)],
    [sg.Text('_'  * 80)],
    [sg.Text("This application is used for examination monitoring")],
    [sg.Text("Press 'START' to start monitoring",justification= "centre")] ,
    [sg.Button("Start",size=(20, 3), key = "Start")] ,
    #sg.Button("Exit", size=(10, 1),key = "Exit")],
    [sg.Text('_'  * 100)],
    [sg.Text('_'  * 100)]
    ]

    pagelayout = [[sg.Column(layout_column, element_justification='center')]]

    rowfooter = [[sg.Image(filename="uonlogo.png",size= (700,200), key="-IMAGEBOTTOM-"),sg.Text('  ')],
                [sg.Text("© University of",justification= "centre")]
                ]
    footerlayout = [[sg.Column(rowfooter, element_justification = 'centre')]]

    layout = [pagelayout, footerlayout]

    window = sg.Window("Exam monitoring homepage", layout, size=(750,450))


    while(True):
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break

        if event == "Start":
            #for i in range(10000):
                #sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='green', transparent_color='green',time_between_frames=1000)
        #sg.PopupAnimated(None)
        #confirm_window()
            webcam_window()
            window.close()


        
           
def webcam_window():
    
    # Camera Settings
    
   #Initialize video capture
    cap = cv2.VideoCapture(0)
    i = 0

    #scaling factor
    scaling_factor = 1.5
    # init Windows Manager
    sg.theme("LightBlue4")

    # def webcam col
    colwebcam1_layout = [[sg.Text("Examination Camera View", size=(30, 1),font=("Helvetica", 25), justification="center")],
                        [sg.Text('_'  * 100)],
                        [sg.Text('Ensure you are in a well lit room',size = (30,1), font = ('Any 15'))],
                        [sg.Text('_'  * 100)],
                        [sg.Image(filename="", key="cam1")],
                        [sg.Text('_'  * 100)]
                        ]
    colwebcam1 = sg.Column(colwebcam1_layout, element_justification='center')

    colslayout = [colwebcam1]

    layout = [colslayout]

    window    = sg.Window("Examination Video Capture", layout, 
                        no_titlebar=False, alpha_channel=1, grab_anywhere=False, 
                        return_keyboard_events=True, size=(750, 550), modal = True)
    while(True):    
        ret, frame = cap.read()  # Capture the current frame
        # Resize the frame
        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        # Display the image
        cv2.imshow('Webcam', frame)
        out_path = "C:/Users/Ceere/Documents/computer Science/fourth year docs/project/projectcodefinal/examimages"
        path = out_path 
        frame_name = str(i)+'.jpg'
        cv2.imwrite(os.path.join(out_path, frame_name), frame)
        i += 1

        # Detect if the Esc key has been pressed
        c = cv2.waitKey(1)
        if c == 27:
            break

# Release the video capture object
    cap.release()
# Close all active windows
    cv2.destroyAllWindows()
    prog_window()

def prog_window():
    sg.theme('LightBlue4')
    layout_column= [
    [sg.Text("Confirm finalization of examination" ,justification="centre",size=(30, 1),font=("Helvetica", 25))],
    [sg.Text('_'  * 80)],
    [sg.Text('Please enter your Registration Number without the fowardslash')],
    [sg.Text('Registration Number', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
    ]

    pagelayout = [[sg.Column(layout_column, element_justification='center')]]

    rowfooter = [[sg.Image(filename="uonlogo.png", size= (700,200),key="-IMAGEBOTTOM-"),sg.Text('  ')],
                [sg.Text("© University of Nairobi",justification= "centre")]
                ]
    footerlayout = [[sg.Column(rowfooter, element_justification = 'centre')]]

    layout = [pagelayout, footerlayout]

    window = sg.Window("Test Image Page-Face API", layout, modal = True)

    while(True):
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            window.close()
            break

        window.close()
    

if __name__ == "__main__":
    main()