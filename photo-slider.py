from customtkinter import *
from PIL import Image

window = CTk()
window.geometry('600x500')

counter = 1

def right():
    global counter
    counter +=1
    if counter > 3:
        counter = 1
    image = Image.open(f'img/space{counter}.jpg')
    image_ctk = CTkImage(light_image=image, size=(600, 400))
    photo.configure(image=image_ctk)

def left():
    global counter
    counter -=1
    if counter < 1:
        counter = 1
    image = Image.open(f'img/space{counter}.jpg')
    image_ctk = CTkImage(light_image=image, size=(600, 400))
    photo.configure(image=image_ctk)


image = Image.open('img/space1.jpg')
image_ctk = CTkImage(light_image=image, size=(600, 400))

photo = CTkLabel(window,text='',  image=image_ctk)
photo.grid(row=0,column=0,columnspan=2)

btn_left = CTkButton(window,text='👈', command=left)
btn_left.grid(row=1,column=0)
btn_right = CTkButton(window,text='👉', command=right)
btn_right.grid(row=1,column=1)


window.mainloop()