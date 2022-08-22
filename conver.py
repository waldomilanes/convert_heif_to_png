from PIL import Image
import pillow_heif
import os

def convert_img(file_name):
    heif_file = pillow_heif.read_heif(file_name)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",

    )
    image.save(file_name[0:-5] + '.png', format("png"))


def runner():
    directory = os.getcwd()
    for filename in os.listdir(directory):
        print('Converting %s...' % os.path.join(directory, filename))
        if filename.lower().endswith(".heic"):
            print('Converting %s...' % os.path.join(directory, filename))
            convert_img(filename)
            continue

runner()