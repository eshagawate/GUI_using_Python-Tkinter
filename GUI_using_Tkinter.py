from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk,Image
from tkinter import messagebox
from functools import partial
from PIL import ImageTk, Image 


root =Tk()
root.title("PAWFECT - A COMPLETE PET SHOP")


img =Image.open('bg.jpg')
img=img.resize((7000,5000))
bg = ImageTk.PhotoImage(img)

#Add image
label = Label(root, image=bg)
label.place(x=0,y=0,width=8000,height=1000)

life=Image.open('lifestyle.jpg')
life=life.resize((600,150))
my_life= ImageTk.PhotoImage(life)
Life_1= Label(image=my_life)
Life_1.place(x=880,y=50)

cat=Image.open('categories.jpg')
cat=cat.resize((500,125))
my_cat= ImageTk.PhotoImage(cat)
cat_1= Label(image=my_cat)
cat_1.place(x=950,y=620)


w = Label(root,text = "Welcome to 'PAWFECT' -- A one stop solution for pet shopping",font=('Helvetica 20 bold'))
w.pack(pady=10)


I=Image.open('sign_up.jpg')
I=I.resize((80,50))
my_I= ImageTk.PhotoImage(I)
L_1= Label(image=my_I)
L_1.place(x=250,y=90)


s=Button(root,text='Sign up',compound='left')
s.place(x=250,y=150) 

    
Im=Image.open("sign_in.jpg")
Im=Im.resize((80,50))
my_Im= ImageTk.PhotoImage(Im)
L_12= Label(image=my_Im)
L_12.place(x=150,y=90)

l=Button(root,text='Sign in',compound='left')
l.place(x=150,y=150)


#Menu:
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open Cart ')
filemenu.add_command(label='Wishlist')
filemenu.add_separator()
filemenu.add_command(label='Exit', command= root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu= helpmenu)
helpmenu.add_command(label='About')


img2=Image.open('bitty.jpeg')
img2=img2.resize((300,400))
my_img2= ImageTk.PhotoImage(img2)
my_label2= Label(image= my_img2)
my_label2.pack(side=LEFT)

img3=Image.open('tango.jpeg')
img3=img3.resize((300,400))
my_img3= ImageTk.PhotoImage(img3)
my_label3= Label(image= my_img3)
my_label3.pack(side=LEFT)

img4=Image.open('Shop_by_brands.jpg')
img4=img4.resize((700,400))
my_img4= ImageTk.PhotoImage(img4)
my_label4= Label(image= my_img4)
my_label4.pack(side=RIGHT)


def Submit():
    messagebox.askquestion("Dog's Food","Do you want to be redirected to Food's page?")
    root.geometry("100x100")
  

    
img_food=Image.open('food.jpg')
img_food= img_food.resize((150,150))
f=ImageTk.PhotoImage(img_food)
b=Button(root,text='Food',image=f,compound='top',command = Submit)
b.pack(anchor=CENTER)


def Submit1():
    messagebox.askquestion("Dog's Collar","Do you want to be redirected to Collar's page?")
    root.geometry("100x100")
   

img_food1=Image.open('collar.jpg')
img_food1= img_food1.resize((150,150))
c=ImageTk.PhotoImage(img_food1)
Button(root,text='Collar',image=c,compound='top',command=Submit1).pack()


def Submit2():
    messagebox.askquestion("Dog's Bed","Do you want to be redirected to Bed's page?")
    root.geometry("100x100")

    

img_food2=Image.open('bed.jpg')
img_food2= img_food2.resize((150,150))
b=ImageTk.PhotoImage(img_food2)
Button(root,text='Bed',image=b,compound='top',command=Submit2).pack()

img_food3=Image.open('shampoo.jpg')
img_food3= img_food3.resize((150,150))
b1=ImageTk.PhotoImage(img_food3)
Button(root,text='Shampoo',image=b1,compound='top').pack()


root.mainloop()
