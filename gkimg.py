#!/bin/python
import numpy as np
import matplotlib.pyplot as plt
import cv2, sys
from tkinter import *
import customtkinter as ctk
import CTkMessagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

FILETYPES = (("JPG", "*.jpg"), ("JPEG", "*.jpeg"), ("PNG", "*.png"), ("All files", "*.*"))
HEIGHT = 250
WIDTH = 430

filename = ''
segImg = None
origImg = None

def openImg():
	global origImg, filename, lbl, FILETYPES
	filename = ctk.filedialog.askopenfilename(initialdir='~',title="Select an image",filetypes=FILETYPES)
	if filename:
		origImg = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB)
		lbl.configure(text=filename.split('/')[-1])
def saveImg():
	global segImg, origImg, filename, FILETYPES
	savename = ctk.filedialog.asksaveasfilename(initialdir='~',title="Save file",filetypes=FILETYPES)
	if savename:
		plt.savefig(savename, dpi=300, bbox_inches='tight')
		origImg = None
		segImg = None
		filename = ''
		lbl.configure(text='No file loaded')
def generateImg():
	global entry, root, filename, segImg, origImg, imgFrame
	k = entry.get()
	if not (k.isdecimal() and int(k) > 0):
		CTkMessagebox.CTkMessagebox(title='Error', message='K is not valid.', icon='warning', width=40, height=25)
	elif origImg is None:
		CTkMessagebox.CTkMessagebox(title='Error', message='No file selected.', icon='warning', width=40, height=25)
	else:
		fig = Figure(figsize=(5, 5), dpi=45)
		plot = fig.add_subplot(111)
		pixVals = np.float32(origImg.reshape((-1,3)))
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
		retval, labels, centers = cv2.kmeans(pixVals, int(k), None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
		centers = np.uint8(centers)
		segData = centers[labels.flatten()]
		segImg = segData.reshape((origImg.shape))
		canvas = FigureCanvasTkAgg(fig, master=imgFrame)
		plot.axis('off')
		plt.axis('off')
		plot.imshow(segImg)
		plt.imshow(segImg)
		canvas.draw()
		canvas.get_tk_widget().grid(column=2, row=3)
ctk.set_appearance_mode('dark')
root = ctk.CTk()
root.geometry('{}x{}'.format(WIDTH, HEIGHT))
root.grid()

ctlFrm = ctk.CTkFrame(master=root)
ctlFrm.grid(column=0, row=0, padx=10, pady=10)

inFrm = ctk.CTkFrame(master=ctlFrm)
inFrm.grid(column=0, row=0, pady=5, padx=5)

ctk.CTkLabel(master=inFrm, text='K: ').grid(column=0, row=0)
entry = ctk.CTkEntry(master=inFrm)
entry.grid(column=1, row=0)

lbl = ctk.CTkLabel(master=ctlFrm, text='No file loaded.')
lbl.grid(column=0, row=3, pady=5, padx=5)

ctk.CTkButton(master=ctlFrm, text='Open image', command=openImg).grid(column=0, row=4, pady=5)
ctk.CTkButton(master=ctlFrm, text='Generate image', command=generateImg).grid(column=0, row=5, pady=5)
ctk.CTkButton(master=ctlFrm, text='Save image', command=saveImg).grid(column=0, row=6, pady=5)

imgFrame = ctk.CTkFrame(master=root)
imgFrame.grid(column=1, row=0, pady=10)

root.mainloop()