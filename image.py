from PIL import Image
import os


for file in os.listdir('orig'): # listdir : list all the files in the folder that this python file located # '.' means 現在位置 # '資料夾名稱'
    if file.endswith('.jpeg'): # endswith : 字串特有的、檢查是否以''為結尾的功能
        # image_file = Image.open('orig/' + file) # 粗糙的路徑合併作法
        image_file = Image.open(os.path.join('orig', file)) # open colour image # os.path.join() : join the path
        image_file = image_file.convert('L') # convert image to grey scale
        image_file.save('result/' + file[:-5] + '_grey.png')