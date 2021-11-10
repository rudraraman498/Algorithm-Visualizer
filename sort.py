from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from tkinter import messagebox

root=Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("900x600+200+80")
root.config(bg="lightblue")
data=[]
def StartAlgorithm():
    global data
    bubble_sort(data, drawData, speedscale.get())
    drawData(data, ['green' for x in range(len(data))])
    messagebox.showinfo("Completed","Sorting Complete")
        
def drawData(data,colorArray):
	canvas.delete("all")
	canvas_height=450
	canvas_width=870
	x_width=canvas_width/(len(data)+1)
	offset=10
	spacing_bet_rect=10
	normalised_data=[i /max(data) for i in data]
	
	for i,height in enumerate(normalised_data):
		x0=i*x_width + offset + spacing_bet_rect
		y0=canvas_height - height * 400
		x1=(i+1)*x_width
		y1=canvas_height
		
		canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
		canvas.create_text(x0,y0,anchor=SW,text=str(data[i]),fill="orange")
	root.update_idletasks()

def Generate():
	global data
	minivalue=int(minvalue.get())
	maxivalue=int(maxvalue.get())
	sizeevalue=int(sizevalue.get())
	
	data=[]
	for _ in range(sizeevalue):
		data.append(random.randrange(minivalue,maxivalue+1))
	drawData(data,['red' for x in range(len(data))])

selected_algorithm=StringVar()

random_generate = Button(root,text="Generate",bg="green",relief=SUNKEN,bd=5,width=10,command=Generate)
random_generate.place(x=750,y=60)

sizevaluelabel=Label(text="Size:", bg='DarkSeaGreen4',width=10,relief=GROOVE,bd=5,pady=6)
#sizevaluelabel.place(x=0,y=60)
sizevaluelabel.place(x=20,y=60)


sizevalue=Scale(root,from_=3,to=30,resolution=1,orient=HORIZONTAL,relief=GROOVE,bd=2,width=10)
sizevalue.place(x=120,y=60)

minvaluelabel=Label(text="Min value:", bg='DarkSeaGreen4', width=10,relief=GROOVE,bd=5,pady=6)
#minvaluelabel.place(x=250,y=60)
minvaluelabel.place(x=280,y=60)

minvalue=Scale(root,from_=0,to=10,resolution=1,orient=HORIZONTAL,relief=GROOVE,bd=2,width=10)
minvalue.place(x=370,y=60)


maxvaluelabel=Label(text="Max value:", bg='DarkSeaGreen4', width=10,relief=GROOVE,bd=5,pady=6)
#maxvaluelabel.place(x=500,y=60)
maxvaluelabel.place(x=530,y=60)

maxvalue=Scale(root,from_=11,to=100,resolution=1,orient=HORIZONTAL,relief=GROOVE,bd=2,width=10)
maxvalue.place(x=620,y=60)


start= Button(root,text="Start",bg="green",relief=SUNKEN,bd=5,width=10,command=StartAlgorithm)
start.place(x=750,y=0)

speedlabel=Label(text="Speed :", bg='DarkSeaGreen4', width=10,relief=GROOVE,bd=5,pady=6)
#speedlabel.place(x=400,y=0)
speedlabel.place(x=20,y=10)


speedscale=Scale(root,from_=0.1,to=3.0,resolution=0.2,length=200,digits=2,orient=HORIZONTAL,relief=GROOVE,bd=2,width=10)
speedscale.place(x=120,y=10)


canvas = Canvas(root,width=870, height = 450,bg="black")
canvas.place(x=10,y=130)
root.mainloop()
