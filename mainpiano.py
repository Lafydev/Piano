#2021-11-07  lafy  <lafy@mailo.com>

from tkinter import *
from math import *
from functools import partial
import modsound
import time

n_octave=3
x0,y0=1,10  #left and top margin
w,h=36,150  #keys
space=6     #add space between black keys 
black_keys=[0,1,3,4,5]
Min=48

class DrawPiano():
	
	def __init__(self,master): 
		
		self.root=master
		self.root.title("Piano")
		
		self.can_piano = Canvas (self.root, bg='light gray', height=180, width=755)
		self.can_piano.pack(side =TOP, padx =10, pady =10)
		
		
		self.draw_white_keys()
		self.draw_black_keys()
		self.highlight_white_key(7,"lightyellow")   #CMedium
		self.can_piano.create_text(x0+7*w+2*space,y0+h-2*space,text="C")
		
		
		self.Mframe=LabelFrame(self.root,text="Major Triads",bd=2,bg="#d0d0d0",relief=FLAT)
		self.Mframe.pack(side=TOP)
		
		chords_M=["C ","C #/Db ","D ","D# /Eb ","E ","F ","F# /Gb ","G ","G# /Ab ","A ","A# /Bb ","B "]
		for i in range(len(chords_M)) :
			self.btnM= Button(self.Mframe, text =chords_M[i],command=partial(self.chords_M,i))
			self.btnM.pack(side=LEFT)
			
		self.mframe=LabelFrame(self.root,text="Minor Triads",bd=2,bg="#d0d0d0",relief=FLAT)
		self.mframe.pack(side=TOP)
		
		chords_m=["Cm","Cm#/Dmb","Dm","Dm#/Emb","Em","Fm","Fm#/Gmb","Gm","Gm#/Amb","Am","Am#/Bmb","Bm"]
		for i in range(len(chords_m)) :
			self.btnm= Button(self.mframe, text =chords_m[i],command=partial(self.chords_m,i))
			self.btnm.pack(side=LEFT)
		
		self.mframe=LabelFrame(self.root,text="Progressions",bd=2,bg="#d0d0d0",relief=FLAT)
		self.mframe.pack(side=TOP)
			
		#self.btn_melody=Button(self.root,text='Play a melody',command=sound.melody)
		#self.btn_melody.pack(side=TOP)
		
		self.msg=Label(self.root,text="")
		self.msg.pack(side=TOP)
		
		#self.Btn1= Button(self.root, text ='Quit', command =self.end)
		#self.Btn1.pack(side=RIGHT)
		
		self.can_piano.bind("<Button-1>",self.clic_note) #look at mouse events
		
		
	
	def draw_white_keys(self):

		i=0
		while (i<=7*n_octave-1):
			self.can_piano.create_rectangle (x0+i*w, y0,x0+(i+1)*w, y0+h,outline="black",fill="white")
			i=i+1		
		
	def draw_black_keys(self):	
		i=0
		while (i<7*n_octave):	
			if ((i%7) in black_keys):
				self.can_piano.create_rectangle (x0+i*w+w/2+space, y0,(i+1)*w+w/2-space, y0+h/2+space,outline="gray",fill="black")

			i=i+1	
			
	def highlight_white_key(self,num,color):
		self.can_piano.create_rectangle (x0+num*w, y0,(num+1)*w, y0+h,outline="gray",fill=color)
		if (num%7 in black_keys): 
			self.highlight_black_key(num,"black")
		if ((num-1)%7 in black_keys) :
			self.highlight_black_key(num-1,"black")
	
	def highlight_black_key(self,num,color):
		self.can_piano.create_rectangle (x0+num*w+w/2+space, y0,(num+1)*w+w/2-space, y0+h/2+space,outline="gray",fill=color)
		
	def is_white_key(self,i,mvtx,mvty):
		key= (i-x0)/w
		if ((i<mvtx<i+w) and (y0<=mvty<=h+y0+space)):
			return True
		else: 
			return False
		 	
	def is_black_key(self,i,mvtx,mvty):
		key= (i-x0)/w 
		if (i+w/2+space<mvtx<i+w+w/2-space)	and (y0<=mvty<=h/2+y0+space) and ((int(key)%7) in black_keys):
			return True
		else: 	
			return False
	
	def find_key(self,mvtx,mvty):
		i=x0
		num_note=-1
		while (i<= x0+w*7*n_octave) and (num_note==-1):
			key =(i-x0)/w 
			if self.is_black_key(i,mvtx,mvty):
				num_note=key+0.5
				black=True
			#elif self.is_black_key(i-w/2,mvtx,mvty):
			#	num_note=key-0.5
			#	black=True
			elif self.is_white_key(i,mvtx,mvty):
				num_note=key
			else:
				i=i+w
		self.msg.configure(text="key "+str(num_note))	
		return (num_note)
			
	def clic_note(self,event):
		mvtx=int(event.x)
		mvty=int(event.y)
		#self.msg.configure(text="clic "+str(mvtx)+"-"+str(mvty))
		
		num_note=self.find_key(mvtx,mvty)
		
		output= self.convert_key(num_note)
		
		sound.play_note(output)
			
	def convert_key(self,num):
		output=48
		if (num>=7):                         
			output=output+12*int(num/7)
			num=num%7
		in_keys=[0,0.5,1,1.5,2,3,3.5,4,4.5,5,5.5,6]
		for index in range(len(in_keys)):
			if num==in_keys[index]:
				#print(output+index)
				return(output+index)
				
	def chords_M(self,i):	
		#print("chord_M"+str(i))
		sound.play_chord_M(i)
	
	def chords_m(self,i):	
		sound.play_chord_m(i)	
	
	def end(self):
		sound.quit()
		self.root.destroy()
		
	
class DrawCircle():
	def __init__(self,master):
		self.root=master 
		self.can_fifth = Canvas (self.root, bg='light gray', height=340, width=340)
		self.can_fifth.pack(side =TOP, padx =10, pady =10)
		
		self.draw_fifth()
		self.can_fifth.bind("<Button-1>",self.clic_circle) #events on fifth cicle
		
		self.msgcircle=Label(self.root,text="")
		self.msgcircle.pack(side=TOP)
		
	def draw_fifth(self):
		ri=80
		r=120
		R=160
		xc,yc=175,175
		self.can_fifth.create_oval(xc-ri,yc-ri,xc+ri,yc+ri,outline="black",fill="violet")
		self.can_fifth.create_oval(xc-r,yc-r,xc+r,yc+r,outline="navy",width="2")
		self.can_fifth.create_oval(xc-R,yc-R,xc+R,yc+R,outline="navy",width="2")
		
		fifth_M=["C","G","D","A","E","B","F#","Db","Ab","Eb","Bb","F"]
		fifth_m=["Am","Em","Bm","F#m","Dbm","G#m","D#m","Bbm","Fm","Cm","Gm","Dm"]
		i=0
		while(i<=11):
			#rotate (-pi/2)
			x1= xc+(r+15)*sin(i*pi/6)
			y1= yc-(r+15)*cos(i*pi/6)
				
			self.can_fifth.create_text(x1,y1,text=fifth_M[i],anchor=CENTER)
			
			x2= xc+(ri+15)*sin(i*pi/6)
			y2= yc-(ri+15)*cos(i*pi/6)
			self.can_fifth.create_text(x2,y2,text=fifth_m[i],anchor=CENTER)
			
			i=i+1	
			
	def clic_circle(self,event):
		xc,yc=175,175
		r0=120
		r=sqrt(pow(event.x-xc,2) + pow(event.y-yc,2) )
		mvtx=(event.x-xc)/r
		mvty=(event.y-yc)/r
		#self.msgcircle.configure(text="clic x="+str(mvtx)+" y="+str(mvty))
		
		
		if  (-1<((mvtx)) <1):
			x=round(10*(asin(mvtx) )/6 )
		else:
			x=0
		if  (-1<((mvty)) <1):	
			y =round(10* (acos(-mvty) /6 ))
		else:
			y=0
		self.msgcircle.configure(text="x="+str(x)+" y="+str(y))
		couple=[(0,0),(1,1),(2,2),(3,3),(2,3),(1,4),(0,5),(-1,4),(-2,4),(-3,3),(-2,2),(-1,1)]
		#fifth_M=["C","G","D","A","E","B","F#","Db","Ab","Eb","Bb","F"]
		#chords_M=["C ","C #/Db ","D ","D# /Eb ","E ","F ","F# /Gb ","G ","G# /Ab ","A ","A# /Bb ","B "]
		fifth_M_order=[0,7,2,9,4,11,6,1,8,3,10,5]
		
		#fifth_m=["Am","Em","Bm","F#m","Dbm","G#m","D#m","Bbm","Fm","Cm","Gm","Dm"]
		fifth_m_order=[9,4,11,6,1,8,3,10,5,0,7,2]
		
		for index in range(len(couple)):
				if (x,y) == couple[index]:
					if r>= r0:
						print("index="+str(index)+", fifth="+str(fifth_M_order[index]) )
						sound.play_chord_M(fifth_M_order[index])
					else:
						sound.play_chord_m(fifth_m_order[index])	
	
		
			
			
#main
if __name__ == '__main__':
	root=Tk()
	sound=modsound.PlaySound()
	mypiano=DrawPiano(root)
	mycircle=DrawCircle(root)
	root.mainloop()   

