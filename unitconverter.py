from tkinter import *
root=Tk()

def cm2m():
    cm=float(input("value in cm : "))
    x=(cm/100)
    print(x,' meter')

def m2cm():
    m=float(input(" value in meter : "))
    print(m*100,' cm')


def k2cel():
    kel=float(input("value in kelvin : "))
    x=kel-273.15
    print(x,' celcious')

def cel2k():
    cel=float(input(" value in celcious : "))
    print(cel+273.15,' kelvin')



bcm2m=Button(root,text="cm2m",command=cm2m)
bcm2m.pack()

bm2cm=Button(root,text="m2cm",command=m2cm)
bm2cm.pack()

bk2cel=Button(root,text="k2cel",command=k2cel)
bk2cel.pack()

bcel2k=Button(root,text="cel2k",command=cel2k)
bcel2k.pack()


root.mainloop()