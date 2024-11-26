from PIL import Image
from PIL.ExifTags import TAGS 
from datetime import datetime
import os
import shutil # To copy files

dir = "/Users/dvasani/Documents/Photos/"

def get_exif_data(dir):
    photo_date_time = {}

    file_names = os.listdir(dir)  
    for file_name in file_names:
        if(os.path.isfile(file_name)):

            file_path = os.path.join(dir, file_name)
            
            # Get Image object, Check if it is only image file.
            # It will fail for dir.
            
            image = Image.open(file_path)
        

            # Get EXIF data
            exif_data = image.getexif()

            # Convert TAGS to human readable
            for tag_id in exif_data:
                tag = TAGS.get(tag_id, tag_id)
                if (tag == 'DateTime'):
                    data = exif_data.get(tag_id)
                    photo_date_time[file_name] = data
      
    return photo_date_time
    


########################################################################################################
#   Get Photo EXIF data
########################################################################################################
data = get_exif_data(dir)

date_format = "%Y:%m:%d %H:%M:%S" 


########################################################################################################
#  Once you have EXIF DATA for each photo
#  Create Directory as per Year, Month like 2023
#                                               1
#                                               2
#                                            2024
#                                               6
# Finally construct source path , destination path and MOVE files      
########################################################################################################

for photo,time_stamp in data.items():
    dt = datetime.strptime(time_stamp, date_format)
    target_dir = dir + str(dt.year) + '/' + str(dt.month) + '/'
    
    # Create directory if not crated from EXIF date
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Now construct source and destination path
    source_path = dir + photo
    target_path =  target_dir + str(dt.year) + "-" + str(dt.month) + "-" +  str(dt.day) + '_' + str(dt.hour) + "-" + str(dt.minute) + "-" + str(dt.second) + '.jpg'
    
    if os.path.isfile(source_path):
        shutil.move(source_path, target_path)


    print(source_path, target_path)








