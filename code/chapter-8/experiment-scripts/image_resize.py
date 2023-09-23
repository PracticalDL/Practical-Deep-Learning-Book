from PIL import Image
import os


def get_file_size(filename):
    stats = os.stat(filename)
    return stats.st_size


filename = "ObamaSpeech.jpg"
image = Image.open(filename)
print((filename, get_file_size(filename), image.size))

size_factor = 100
while size_factor > 5:
    size_factor -= 5
    size = tuple([size_factor * x / 100 for x in image.size])
    modified_filename = (
        "Resize/" + filename + "_Size_" + str(size[0]) + "x" + str(size[1]) + ".jpg"
    )
    modified_image = image.resize(size, Image.LANCZOS)
    modified_image.save(modified_filename, format="JPEG")
    print((modified_filename, get_file_size(modified_filename)))
