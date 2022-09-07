import PySimpleGUI as sg
import os
import cv2
from PIL import Image, ImageTk
from PIL import Image



def govt_input():
    sg.theme('LightBlue4')

    # Very basic window.
    # Return values using
    # automatic-numbered keys
    layout = [
        [sg.Text('Please enter your Registration Number without the fowardslash')],
        [sg.Text('Registration Number', size=(15, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Registration number Input Window', layout)
    event, values = window.read()
    window.close()

    # The input data looks like a simple list
    # when automatic numbered
    reg_num = values[0]
    print(reg_num,type(reg_num))
    return reg_num
    #print(event)

def check_student_image_db(reg_number):
    student_image_db = 'student_repository'  # dummy folder rep govt db of images

    for filename in os.listdir(student_image_db):
        #print(f'Filenames are:- {filename}')
        if filename.startswith(reg_number):
            sg.theme("DarkGreen")
            sg.popup("User found")
#
            print('User found')
            p = filename
    return p
        


reg_number = govt_input()

p = check_student_image_db(reg_number)


image_path = f'student_repository/{p}'
image_cv2 = cv2.imread(image_path)
#saving image to test folder
saved_govt_img = cv2.imwrite(r'testimage/testimage.png', image_cv2)

#converting test image and saving as thumbnail
image = Image.open('testimage/testimage.png')
image.thumbnail((110,110))
image.save('testimage/testimagethumbnail.png')
 #converting frame 5 captured and saving as randomimage
image = Image.open('5.png')
image.thumbnail((110,110))
image.save('testimage/framethumbnail.png')
#converting test image for display
image = Image.open('testimage/testimage.png')
image.thumbnail((250,250))
image.save('testimage/viewtest.png')




