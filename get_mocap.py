# Not relevant for the current folder. This was used to extract all mocap data from the expressive musical gestures dataset.

from glob import glob
import shutil
import os

mocap_files = glob("piano/*/dataset/*/mocap.csv") # Select all mocap files

# Loop over the files
for src in mocap_files:
    params = src.split("/")
    pianist = params[1]
    style = params[3]
    dst = f"mocap_data/{pianist}/{style}_mocap.csv" 

    shutil.copyfile(src, dst) # Save all mocap files in one folder, sorted by pianist; each file's name indicates the style and recording number (e.g. NOMETRO_NORMAL_NORMAL_1)
