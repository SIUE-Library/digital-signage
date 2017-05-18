# Raspberry Pi Slideshow
## Description
This program is a slideshow that automatically starts when the Raspberry Pi is turned on and will constantly cycle through images until turned off.
## Intended to be used with either:
-Raspberry Pi 2 **-OR-** Raspberry Pi 3

## Verified working operating systems:
#### Raspberry Pi 2:
Ubuntu MATE Desktop for Raspberry Pi 2 
> https://ubuntu-mate.org/raspberry-pi/

#### Raspberry Pi 3:
Ubuntu MATE Desktop for Raspberry Pi 3 
> https://ubuntu-mate.org/raspberry-pi/

**NOTE**: Although the program may seem to work on other operating systems, these systems have not been fully tested and may have issues. 

## Installation of Operating System:
Both download links listed above will return a zipped img file of the operating system, and this will need to be installed to a microSD on a different computer in order to be ran on the Pi.

If you are unsure on how to install an operating system to an external drive, a helpful guide can be found at 
> https://www.raspberrypi.org/documentation/installation/installing-images/

After installing your operating system, verify that the Pi turns on and boots correctly. If you have any troubles with this, another helpful guide can be found at 
> https://www.raspberrypi.org/forums/viewtopic.php?t=58151

When setting up your operating system for the first time, make sure you **check the box to log-in automatically**, otherwise you will need to log on **manually each time** you start on the pi. 
The current script also assumes the user name has been set to "ubuntu". This can be changed, however, by modifying the file path where necessary in the scripts.

## Preparing the Pi to run the program:
The Python script has a few dependencies and a few extra utilities will need to be installed in order for this program to run properly. These can be installed using the `apt-get` command in terminal. This requires an internet connection to download, although the program itself will not require a connection to run.

### Utilities:
| Utility Name | Description |
| ------------ | ------------|
| `gnome-terminal`| Necessary in order to run the script on boot|

### Python Libraries:
**This program uses Python 2**, and assumes it is installed with your operating system. It also requires the following libraries to be installed.
| Library |
|-------------|
|`python-tkinter`|
|`python-imaging`|
|`python-imaging-tk`|

Once you have installed the proper utilities and libraries, you can simply drop the entire "slides" directory into your home directory ("/home/ubuntu" in our case") You will also need to make the `execslides.sh` script executable through the properties menu on the right-click.

Lastly, you will need to set `execslides.sh` to boot at start. This process will vary depending on the operating system you use, but for Ubuntu MATE, it is as simple as going to the control center, searching for "Startup Applications" and adding a new program with the command `/home/ubuntu/slides/execslides.sh` 
The name and comment can be whatever you like, but we recommend naming it something memorable and easily identifiable, in case of later troubleshooting.

## Adding pictures and running your program:
Any images that you would like to play in the slideshow should be added to the "gallery" folder in the "slides" directory. The program will automatically draw anything from that folder into the slideshow.  The pool of images the programs draws from is refreshed each time the image updates, so any images that are added to the folder will be added to the slideshow immmediatly; there is no need to restart the program.

**NOTE:  Currently only images with extensions .gif, .jpg, .jpeg, and .png will be used.  Any other file in the gallery directory will be ignored.  You can manually modify the program to accept other file types (see in-code comments) however we make no guarantees these will be supported by tkinter**

After you have loaded your images, simply reboot your computer and the your slideshow should automatically start on boot.
To cancel your slideshow and return to the desktop, press either `CTRL + c` or `ALT + F4` to escape the program.

## Miscellanous Notes
The mouse will be automatically hidden by the program.  It is invisible during runtime, but still technically exists.
Left clicking will automatically progress the slideshow one image.  This also reset the timer that controls image changing.  This is useful for quickly navigating the slideshow.

Most parameters you may want to change are explained by the in-code comments.  Even if you don't have a strong knowledge of python or tkinter these should guide you through customizing the program.

As mentioned above, any image added to the folder will be automatically added to slideshow.  It is beyond the scope of this tutorial, but this means you could in theory set up some form of file sharing through NFS/FTP/SSH/etc. to remotely control the program.

This tutorial convered the entire set up of the digital signage: taking you from a factory raspberry pi and completely automating this slideshow.  However this python script also runs well out of box on any computer with the proper python libraries installed.

# DigitalSignage

## Project Team 

- Team Leader: Dale Auten (dauten@siue.edu)
- Team Member: Jake Grubb (jagrubb@siue.edu)
- Project Manager: Sarah Park (gpark@siue.edu)

## LICENSE MIT License
