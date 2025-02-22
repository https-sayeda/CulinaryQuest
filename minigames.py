from tkinter import *

#drawing lines
'''def get_x_and_y(event): #gets x and y coordinates when mouse clicked
    global lasx, lasy 
    lasx, lasy = event.x, event.y 
    #updates the starting coordinates by assinging the value of the end coordinates


def draw_line(event): #draws line on canvas
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), fill="red", width=3)
    lasx, lasy = event.x, event.y


app = Tk()
app.geometry("400x400") #the size of the window
canvas = Canvas(app, bg="black") 
#creating a canvas onto the window with background colour black
canvas.pack(anchor="nw", fill = "both", expand = 1)
#the canvas is anchored at the top left corner of the window and fills the
#entire window

canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_line) 
#calls the functions when left mouse clicked

app.mainloop()'''

