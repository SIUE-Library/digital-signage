#########################################################################
# Original Author:      Dale Auten                                      #
# Date created:         2017-01-23                                      #
# Date modified:        2017-01-30                                      #
# Description:          Plays a slideshow.  This uses every file in the #
#                       relative directory 'gallery/' so there will be  #
#                       errors if there are none-images                 #
#########################################################################



import os                       # needed to get directory
import sys                      # used to exit
import time                     # used to wait
import Tkinter as tk            # GUI
from PIL import Image, ImageTk			# allows GUI to display images

def main():

        # tracks where we are in the list
	counter = 0

        # gets directory name
	dir = os.path.dirname(__file__)+"/gallery/"

        # stores filenames
	list = []

        # go through directory and add all filenames to list
	for filename in os.listdir(dir):
		list.append(filename)

        # if there was nothing there we can't have a slideshow so exit
	if len(list) == 0:
		sys.exit()

        # pick the image from the list we'll use.  we do this now to prevent an error that may happen if a file is deleted
	img = Image.open(dir + list[counter])

        # instantiate GUI
	root = tk.Tk()

	# get screen dimensions
	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()

        # resize image so it fits screen
	img = img.resize((w, h), Image.ANTIALIAS)

	# save image to a different format.  one that the gui can use
	img = ImageTk.PhotoImage(img)

	# create a panel and insert to the image into it
	panel = tk.Label(root, image = img)

	# pack panel into gui
	panel.pack(side = "bottom", fill = "both", expand = "yes")

        # this makes window not have frame and cover taskbar.  required for fullscreen
	root.overrideredirect(1)

	# set window dimensions
	root.geometry("%dx%d+0+0"%(w,h))

        # now we repeat this forever
	while True:

                # empty list and remake it.  this way if an image is added to the folder during execution we
                # can get it and add it immediately
		list = []
		for filename in os.listdir(dir):
			list.append(filename)

		if len(list) == 0:
			sys.exit()

                # increase where we are in the list, and if we are out of bounds reset it
		counter = counter + 1
		if counter >= len(list):
			counter = 0

                # open and load new image
		img = Image.open(dir + list[counter])
		img = img.resize((w, h), Image.ANTIALIAS)
		img = ImageTk.PhotoImage(img)
		panel.configure(image=img)

		# update screen
		root.update_idletasks()

		# wait ABOUT this many seconds.  time.sleep() is imprecise
		time.sleep(12)


# start running
main()
