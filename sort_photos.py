from PIL import Image
from PIL.ExifTags import TAGS 
from datetime import datetime
import os
import shutil # To copy files

dir = "/Users/xyz/Documents/Photos/"

def get_exif_data(dir):
    photo_date_time = {}

    file_names = os.listdir(dir)  
    for file_name in file_names:
        
        if(os.path.isfile(os.path.join(dir,file_name)) and not file_name.startswith('.')):
      
            file_path = os.path.join(dir, file_name)

    
            # Get Image object, Check if it is only image file.
            # It will fail for dir.
            
            image = Image.open(file_path)
        

            # Get EXIF data
            exif_data = image.getexif()

            # Convert TAGS to human readable
            for tag_id in exif_data:
                tag = TAGS.get(tag_id, tag_id)
                #print(tag_id, tag)
                if (tag == 'DateTime'):
                    data = exif_data.get(tag_id)
                    print(tag_id, tag, data)
                    photo_date_time[file_name] = data
       
            print(" ----- ----- ")
          
    return photo_date_time
    


########################################################################################################
#   Get Photo EXIF data
########################################################################################################
data = get_exif_data(dir)

#data = {'IMG_001.jpg': '2024:03:23 13:10:34', 'IMG_002.jpg': '2024:08:23  '}


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

     #data = {'IMG_001': "2015:11:17 10:59:33",'IMG_002': "2017:11:22 14:59:33"}      

for photo,time_stamp in data.items():
    dt = datetime.strptime(time_stamp, date_format)
    target_dir = dir + str(dt.year) + '/' + str(dt.month) + '/'
    #target_dir = "/Users/xyz/Photos/2015/11/"
    #target_dir = "/Users/xyz/Photos/2017/11/"

    
    # Create directory if not created from EXIF date
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Now construct source and destination path
    source_path = os.path.join(dir, photo)
    

    target_path =  target_dir + str(dt.year) + "-" + str(dt.month) + "-" +  str(dt.day) + '_' + str(dt.hour) + "-" + str(dt.minute) + "-" + str(dt.second) + '.jpg'
    
    if os.path.isfile(source_path):
        shutil.copyfile(source_path, target_path)











