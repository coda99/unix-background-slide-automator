#!/usr/bin/python3

import os, sys, time
from file import open_file
from file_sys_manipulator import getpath, getdirname


year, month, day = time.gmtime()[0], time.gmtime()[1], time.gmtime()[2]

### Creating a path and getting external paths
filename = sys.argv[2]
path = getpath()
dir_name = getdirname()
file_save_path = f"{path}/{dir_name}/{filename}"


"""
  This module writes and save the XML file needed for the slide show

  Args:
      List (list : str): Accepts a list of image file names
"""

def xml_writer(List):

  """
    Returns an XML file and saves it to the specified directory given
  """

  ### Removing all new line characters from List
  newline_rm = str.maketrans('', '', '\n')
  List = [s.translate(newline_rm) for s in List]

  to = List[1:]

  try:
    with open(file_save_path, 'w') as f:
      print(
        f"<background>\n"
        f"\t<starttime>\n"
        f"\t\t<year>{year}</year>\n"
        f"\t\t<month>{month}</month>\n"
        f"\t\t<day>{day}</day>\n"
        f"\t\t<hour>00</hour>\n"
        f"\t\t<minute>00</minute>\n"
        f"\t\t<second>00</second>\n"
        f"\t</starttime>",
        file = f
      )

    with open(file_save_path, 'a') as f:
      for k,v in enumerate(List):
        print(
          f"\t<static>\n"
          f"\t\t<duration>1795.0</duration>\n"  
          f"\t\t<file>{path}/{dir_name}/{v}</file>\n"  
          f"\t</static>\n"
          f"\t<transition>\n"
          f"\t\t<duration>5.0</duration>\n"
          f"\t\t<from>{path}/{dir_name}/{v}</from>\n"
          f"\t\t<to>{path}/{dir_name}/{to[k]}</to>\n"
          f"\t</transition>",
          file = f
        )

  except IndexError:
    with open(file_save_path, 'a') as f:
      print(f"</background>", file = f)

if __name__ == '__main__':
  l = open_file("hello.txt")
  xml_writer(l)

