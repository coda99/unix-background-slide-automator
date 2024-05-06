import sys
from file_sys_manipulator import login, dir_maker, user_perm, root_perm
from images import prepare_img, move_img
from xml_writer import xml_writer
from file import open_file

"""
    Main:
        Binds all modules together and runs each part based on steps taken
        to create a wallpaper automator in a Unix based OS
"""

if __name__ == "__main__":
    try:
        if len(sys.argv) < 3 or sys.argv[2][-4:] != '.xml':
            print("usage: <program name> <dir name> <xml filename (foo.xml)>")
        else:
            login()
            prepare_img()
            user_perm()
            dir_maker()
            move_img()
            xml_writer(open_file("images.txt"))
            root_perm()

            print("----------------------------------")
            print("\tProgram Completed")
            print("----------------------------------")
            print()
            print("----------------------------------")
            print("Steps To Activate Automation")
            print("----------------------------------")
            print(
                "Go to Menu >> Preferences >> Appearance >> Background \n"
                "Click on Add >> backgrounds >> '<Your dir name>' \n"
                "Click on the drop down at your bottom right and select 'All files' \n"
                "Double on your XML file to open \n"
            )


    except (IndexError, NameError):
        print("usage: <program name> <dir name> <xml filename>")
