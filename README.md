# unix-background-slide-automator

A Unix background slide automator written in python

## Usage
  main.py < dir name > < xml filename (foo.xml) >

## Program Structure
* Request For Super User access
* Prepares your images (looks at the /images and extract all file names and puts them in a images.txt file)
* Creates your slide directory (which was passed as a command line arg) 
* Moves images from pre-defined images folder to newly created directory
* Writes an XML file (which was pass as a command line arg)

#### Tested on Parrot OS 5.3 (Electro Ara)
