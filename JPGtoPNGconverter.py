import sys
import os
from PIL import Image

# command line args
raw_folder = sys.argv[1]
output_folder = sys.argv[2]

output_folder_exists = os.path.isdir(output_folder)

# check if output folder exists, if not, create
if not output_folder_exists:
  os.mkdir(output_folder)

# loop through raw and convert to png
for file in os.listdir(raw_folder):
  filename = os.path.splitext(file)[0]
  img = Image.open(f'{raw_folder}{file}')
  img.save(f'{output_folder}{filename}.png', 'png')

