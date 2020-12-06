from tkinter import *
import cv2
from firstFrame import FrameCapture
from video import videoAnalyse
import time

# Fenêtre principale
window = Tk()

#Personnalisation
window.title('Traitement de signal')
window.geometry("1080x720")
window.minsize(480, 360)
#window.iconbitmap('') import d'image
window.config(background='grey')


sens = "H"
entree = "up"
toSend = []
video = "Essai"



def nothing(x):
    pass


#Seconde fenêtre fonction

def open_url() :
    FrameCapture()
    originalImage = cv2.imread('./image/frame_0.jpg')
    cv2.namedWindow("Frame")
    cv2.setMouseCallback("Frame", mouse_drawing)
    cv2.imshow("Frame", originalImage)

def newWindow() :
    newWindow = Toplevel(window)
    newWindow.title('Vidéo')
    newWindow.geometry('720x480')
    newWindow.config(background="#4065A4")


def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        if(buttonSens['text'] == "Vertical"):
            sens="V"
            if(buttonEntree['text'] == "Extérieur - Intérieur"):
                entree = "right"
            else:
                entree = "left"
        else:
            sens="H"
            if(buttonEntree['text'] == "Intérieur\nExtérieur"):
                entree = "up"
            else:
                entree = "down" 

        if sens == "H":
            toSend.append(y)
            
        else:
            toSend.append(x)
        toSend.append(sens)
        toSend.append(entree)
        cv2.destroyWindow('Frame')
        videoAnalyse(toSend[0], toSend[1], toSend[2])
    """
    if len(coords) == 1:
        xdiff = abs(coords[0][0] - coords[1][0])
        ydiff = abs(coords[0][1] - coords[1][1])

        if xdiff > ydiff:
            toSend.append(coords[0][1])
            toSend.append("H")
        else:
            toSend.append(coords[0][0])
            toSend.append("V")
        cv2.destroyWindow('Frame')
        videoAnalyse(toSend[0], toSend[1])
"""


#Frame
frameOpen = Frame(window, bg='grey', bd=1)
frameCount = Frame(window, bg='grey', bd=1)

#Text
label_title = Label(window, text="Compteur de passage", 
font=('Arial', 30), bg='grey', fg="white")
label_title.pack(side=TOP)

label_add = Label(frameOpen, text="Ajouter une vidéo", 
font=('Arial', 15), bg='grey', fg="white")
label_add.pack(expand=YES)

label_inPass = Label(frameCount, text="Nombre de personne(s) qui rentre(nt) : ", 
font=('Arial', 15), bg='grey', fg="white")
label_inPass.pack(side=TOP)



#Button
button_add = Button(frameOpen, text="Choisir", font=("Arial",15), bg="white", fg="grey", command=open_url)
button_add.pack(pady=25, fill=X)

def getTextButton():
    if(buttonSens['text'] == "Vertical"):
        buttonSens.config(text="Horizontal")
        buttonEntree.config(text="Intérieur\nExtérieur")
    else:
        buttonSens.config(text="Vertical")
        buttonEntree.config(text="Intérieur - Extérieur")

def setEntree():
    if(buttonEntree['text'] == "Intérieur\nExtérieur"):
        buttonEntree.config(text="Extérieur\nIntérieur")
    elif(buttonEntree['text'] == "Extérieur\nIntérieur"):
        buttonEntree.config(text="Intérieur\nExtérieur")
    elif(buttonEntree['text'] == "Extérieur - Intérieur"):
        buttonEntree.config(text="Intérieur - Extérieur")
    else:
        buttonEntree.config(text="Extérieur - Intérieur")



buttonSens = Button(frameOpen, text="Horizontal", font=("Arial",15), bg="white", fg="grey", command=getTextButton)
buttonSens.pack(pady=40, fill=X)


buttonEntree = Button(frameOpen, text="Intérieur\nExtérieur", font=("Arial",15), bg="white", fg="grey", command=setEntree)
buttonEntree.pack(pady=60, fill=X)

#link = Entry(frameOpen, font=('Arial', 20), bg="#4065A4", fg='white')
#link.pack()

#Input

InPass = Entry(frameCount, font=('Arial', 20), bg="#4065A4", fg='white')
InPass.pack()

label_outPass = Label(frameCount, text="Nombre de personne(s) qui sorte(nt) : ", 
font=('Arial', 15), bg='grey', fg="white")
label_outPass.pack(side=TOP)

OutPass = Entry(frameCount, font=('Arial', 20), bg="#4065A4", fg='white')
OutPass.pack()

#Ajout aux frames
frameOpen.pack(expand=YES)
frameCount.pack(expand=YES)


#Affichage de la fenêtre
window.mainloop()