# Create Virtual Environment. Mac OS Only
## This is just one time steps , to set up virtual Environment, if not created, 
# You do NOT need this for every app you code along.

Select directory, where you will be hosting all the applications, you will be coding along with me.
`python3 -m venv env`
It will create new directory , in which you run above command, check it with:
`ls`
Activate virtual Environment:
`source env/bin/actiate`
Later any time, you want to switch to global environment, type below
`deactivate`


# Install packages
Pillow: This is required to read EXIF data of images.
Follow these steps to install required dependencies.
Go to your virtual environment and activate it.
`pip install -r requirements.txt`

This command will install all the required dependencies.

# Prepare data to run program, copy some of the photos of your to directory
Copy some of the photos to the directory, where program should start reading photos from that directory.

***
Change the **dir variable used in the code to the path to directory on your machine, where photos are stored.
---
---



