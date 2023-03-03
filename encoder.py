# input = test string.
# convert test string to hex values.
# convert string of hex values to list of hex values
# convert list of hex values to rgb values
# create new image with rgb values

from PIL import Image
import math
from sys import argv


# convert string to hexadecimal values
def string_to_hex(text):
    return text.encode().hex()


# convert hexadecimal values to a list of hex values
def hex_string_to_list(string_of_hex_values):
    return [int(string_of_hex_values[i:i+2], 16) for i in range(0, len(string_of_hex_values), 2)]


# convert list of hex values to a list of RGB values
def to_rgb_tuple(list_of_hex_values):
    return list(tuple(list_of_hex_values[i:i+3]) for i in range(0, len(list_of_hex_values), 3))


test_string = argv[1]

# make sure we can have enough bytes for a complete set of RGBA values
remainder = len(test_string) % 3
if remainder == 2:
    # if we have one less than 3 bytes, we add a null byte to even it up
    test_string += chr(0)

hex_string = string_to_hex(test_string)
hex_list = hex_string_to_list(hex_string)
rgb = to_rgb_tuple(hex_list)

# calculate the image dimensions
# the width and height of the image is the rquare root
# of our list length plus 1 to account for any overflow.
image_dimensions = (int(math.sqrt(len(rgb)))+1,
                    int(math.sqrt(len(rgb)))+1)


# create and save the new image
image = Image.new("RGBA", image_dimensions, (0, 0, 0, 0))
image.putdata(rgb)
image.save(argv[2] if argv[2] else "image.png")
