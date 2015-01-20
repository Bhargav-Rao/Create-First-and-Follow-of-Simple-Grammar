from tkinter import *
import os
tk = Tk()
main = Frame(tk,height=5,width=10)
main.pack()
tk.title("First and Follow Set of a Grammar")

label1 = Label( main, text="Input")
t = Text(main,height=10,width=30)
label1.pack()
t.pack()

a=StringVar()
b=StringVar()
c=StringVar()


bottomframe = Frame(tk)
bottomframe.pack( side = BOTTOM )

bottomfollowframe = Frame(bottomframe)
bottomfollowframe.pack( side = RIGHT )
bottomsymbolframe = Frame(bottomframe)
bottomsymbolframe.pack( side = LEFT )



label6 = Label( bottomsymbolframe,text="Symbol")
#label6.pack()
label7 = Message( bottomsymbolframe, textvariable=c,bg="White",fg="Black",relief=RAISED)
#label7.pack()

label2 = Label( bottomframe,text="First")
label3 = Message( bottomframe, textvariable=a,bg="White",fg="Black",relief=RAISED)
#label2.pack()
#label3.pack()
label4 = Label( bottomfollowframe,text="Follow")
#label4.pack()
label5 = Message( bottomfollowframe, textvariable=b,bg="White",fg="Black",relief=RAISED)
#label5.pack()



def getdata():
	file=open('new.txt','w')
	file.write(t.get('1.0','end'))
	#print(t.get('1.0','end'))
	file.close()
	os.system("python3 test.py")
	

	global c
	s = ""
	for i in open("sym.txt").readlines():
		s+=i
	c.set(s)

def first():
	tk.quit
	global a
	s = ""
	for i in open("fst.txt").readlines():
		s+=i
	a.set(s)
	
	label2.pack()
	label3.pack()
	label6.pack()
	label7.pack()
	#def follow():
	global b
	s = ""
	for i in open("fol.txt").readlines():
		s+=i
	b.set(s)
	label4.pack()
	label5.pack()
	

submit = Button(main, text ="Submit Input Grammar", command = getdata)
submit.pack(side =BOTTOM) 
ffirst = Button(main, text ="Find First & Follow ", command = first) #to be replaced by first
submit.pack(side = LEFT)
ffirst.pack(side = LEFT) 
#ffollow = Button(main, text ="Find Follow", command = follow)
#ffollow.pack(side =LEFT)




tk.mainloop()
