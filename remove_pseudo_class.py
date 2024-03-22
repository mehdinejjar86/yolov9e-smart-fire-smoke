import os
from tqdm import tqdm
import sys 



if __name__ == "__main__":
  
  paths = sys.argv[1:]
  files = []

  # Collecting paths of all the labels
  for path in paths:
      files.extend( [os.path.join(path, file) for file in os.listdir(path) if file.endswith(".txt")] )

  
  # Removing Class other (Removing lines with label 1)
  for i in tqdm(range(len(files))):
    # Reading all the lines of a label 
      with open(files[i], "r") as file:
          lines = file.readlines()
  
  for line in reversed(range(len(lines))):
      # Deleting any line with label 1 as it refers to the other class
      if lines[line][0] == "1":
          lines.pop(line)
      # Rewriting all the lines
      with open(files[i], "w") as file:
          for i in range(len(lines)):
              file.write(lines[i])
          
  # To be consistent we need to label the smoke class which is 2 to be 1 
  for i in tqdm(range(len(files))):
      # Reading all the lines of a label
      with open(files[i], "r") as file:
          lines = file.readlines()
      # Chanching any 2 labels with 1 
      for line in reversed(range(len(lines))):
          if lines[line][0] == "2":
              lines[line] = "1" + lines[line][1:]
      # Rewriting all the changes back to the labels
      with open(files[i], "w") as file:
          for i in range(len(lines)):
              file.write(lines[i])
