# gui app

import Tkinter as tk # requires 'apt install python-tk'

window = tk.Tk() # class constructor for window object, main loop inside

text_box = tk.Entry(window) # text entry widget
text_box.pack() # places widget to window using specific method of organisation - in order of packing here

def saveText(): # helper to save text from field to file
	str1 = text_box.get() # gets from text box
	f = open("file1","w")
	f.write(str1.encode("UTF-8")) # encode for polish chars
	f.close()


btn1 = tk.Button(window, text = "Save", command = saveText)
btn1.pack()




window.mainloop()

