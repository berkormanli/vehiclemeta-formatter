import os
import re

pattern = re.compile(r"'[a-z]*\.meta'")

def replacement_function(match):
  print(match.group())
  if match.group().startswith("'data/"):
    print("This item is already in a correct format.")
    return match.group()
  else:
    return "'data/"+match.group()[1:]
 
def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            listdirs(it)
        else:
            if it.name == "fxmanifest.lua":
              print("Editing "+it.path+"...")
              with open(it.path, 'r+') as f:
                data = f.read()
                new_text = re.sub(pattern, replacement_function, data)
                f.seek(0)
                f.truncate(0)
                f.write(new_text)
                f.close()
 
folderDir = input("Please enter the full path of the folder you want to use this tool: ")
listdirs(folderDir)
print("Done!")
