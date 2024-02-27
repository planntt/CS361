import os
from os.path import isfile

# check the current directory and store files in dict
path_to_watch = "."
before = dict([(f, None) for f in os.listdir(path_to_watch) if isfile(f)])
while True:
    # compare before and after dicts to see if files have been added
    after = dict([(f, None) for f in os.listdir(path_to_watch) if isfile(f)])
    added = [f for f in after if f not in before]
    # removed = [f for f in before if f not in after]
    if added:
        print("Added: ", ", ".join(added))
        with open("filename.txt", "w") as outfile:
            newfile = ", ".join(added)
            outfile.write(newfile)

    # if removed:
    #     print("Removed: ", ", ".join(removed))
    before = after
