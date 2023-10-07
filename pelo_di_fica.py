import os
import sys
from PIL import Image

class Img2Pdf:
    supported_estension = ('.jpg', '.pdf', '.jpeg')
    images = []
    width = None
    height = None
    def __init__(self, path):
        self.img_path =  os.path.dirname(path)
        # TODO: Manage the trailing space
        self.pdf_name = f'{os.path.basename(self.img_path)}.pdf'
        self.retrive_image()
    
    def get_image_path(self):
        # TODO: Add support for multiple subfolder
        img_path = []
        for file_path in os.listdir(self.img_path):
            full_file_path= os.path.join(self.img_path, file_path)
            if not os.path.isfile(full_file_path):
                img_path.append(full_file_path+'/')
            else:
                img_path.append(self.img_path)
        return sorted(set(img_path))
  
    def retrive_image(self):
        for file_path in self.get_image_path():
            print(file_path)
            for img_path in sorted(os.listdir(file_path)):
                full_img_path = os.path.join(file_path, img_path)
                if full_img_path.endswith(self.supported_estension):
                    print(full_img_path)
                    img = Image.open(full_img_path)
                    if not self.width and not self.height:
                        self.width, self.height = img.size
                    
                    self.images.append(img.convert('RGB'))
        
    
    def convert(self):
        if self.images:
            pdf = Image.new('RGB', size=(self.width,self.height))
            pdf.save(self.pdf_name, save_all = True, append_images = self.images)
        else:
            print('No images found')


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        response = Img2Pdf(path).convert()
    except IndexError:
        print("You must specify the folder containing the images")
   