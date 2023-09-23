from PIL import Image
import os


def get_file_size(filename):
    stats = os.stat(filename)
    return stats.st_size


filename = "ObamaSpeech.jpg"
image = Image.open(filename)
image = image.rotate(270)
print((filename, get_file_size(filename)))

quality = 10
while quality > 5:
    quality -= 5
    modified_filename = "Compression/" + filename + "_Quality_" + str(quality) + ".jpg"
    image.save(modified_filename, format="JPEG", quality=quality)
    print((modified_filename, get_file_size(modified_filename)))
