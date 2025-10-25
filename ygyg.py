from customtkinter import *
from PIL import Image




win = CTk()
win.geometry("800x600")
win.title('alphsbet')
label = CTkLabel(win, text='alphabet', font=('Arial', 34,'bold'),width=300)
label.grid(row=0,column=0,pady=20,columnspan=2,padx=20)
label_text =CTkLabel(win, text='a', font=('Arial', 200,'bold'),width=300) 
label_text.grid(row=1,column=0,pady=20,padx=20)

img= Image.open('a.jpeg')
img_ctk = CTkImage(light_image=img, size=(400, 400))

label_pictures=CTkLabel(win, text=' ',image=img_ctk, font=('Arial', 200,'bold'),width=300) 
label_pictures.grid(row=1,column=1,pady=20,padx=20)

alphabet=['a','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','S','T','T','U','V','W','X','Y','Z']
i=0
def btn_left_click():
    global alphabet,i
    i=i-1
    if i==0:
        i=len(alphabet)-1
    label_text.configure(text=alphabet[i])
    img= Image.open(alphabet[i]+'.jpeg')
    img_ctk.configure(light_image=img)
    label_pictures.configure(image=img_ctk)
btn_left  = CTkButton(win, text='<<',width=300,font=('Arial', 34, 'bold'),command=btn_left_click)  
btn_left.grid(row=2,column=0,pady=20,padx=20)


def btn_right_click():
    global alphabet,i
    i=i+1
    if i==27:
        i=0
    label_text.configure(text=alphabet[i])
    img= Image.open(alphabet[i]+'.jpeg')
    img_ctk.configure(light_image=img)
    label_pictures.configure(image=img_ctk)
btn_right  = CTkButton(win, text='>>',width=300,font=('Arial', 34, 'bold'),command=btn_right_click)  
btn_right.grid(row=2,column=1,pady=20,padx=20)
win.mainloop()

