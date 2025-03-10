import os
import shutil
import pathlib

class File_organizer:

    def scan_file(self, file_name):
        data = os.listdir(file_name)

        for files in data:
            extension = pathlib.Path(files).suffix
            print("File Extension: ", extension)
   
            if extension == ".jpg":
                if not os.path.exists("jpg_img"):
                    os.mkdir("jpg_img")
                shutil.move(os.path.join(file_name, files), "jpg_img")
            
            elif extension == ".pdf":
                if not os.path.exists("pdf"):
                    os.mkdir("pdf")
                shutil.move(os.path.join(file_name, files), "pdf")
            
            elif extension == ".mp4":
                if not os.path.exists("mp4"):
                    os.mkdir("mp4")
                shutil.move(os.path.join(file_name, files), "mp4")

            else:
                if not os.path.exists("other_type"):
                    os.mkdir("other_type")
                shutil.move(os.path.join(file_name, files), "other_type")
                    
  


if __name__=="__main__":
        
    x = File_organizer()
    x.scan_file( file_name = r"/home/happy/Desktop/Python Projects/ALL")
