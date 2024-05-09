# Linux_Distro-background-slide-automator

A Linux Distro background slide automator written in python

## Usage
  main.py < dir name > < xml filename (foo.xml) >

## Program Structure
* Request For Super User access
* Prepares your images (looks at /images and extract all file names and puts them in a images.txt file)
* Creates your slide directory (which was passed as a command line arg) 
* Moves images from pre-defined images folder to newly created directory
* Writes an XML file (which was passed as a command line arg)

Sample images are included in the images folder, feel free to replace those with desired images

### NOTE
"images" folder must be present in the same directory as main.py and also before running the program make sure you have at least two images in the folder, there is a silent error that occurs and I cannot figure out a way to catch it and stop the program if the images folder is empty, for anyone who would want to take a shot at that, YOU HAVE MY BLESSINGS to do that lol.

#### Tested on Parrot OS 5.3 (Electro Ara)
