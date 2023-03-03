from PIL import Image
from sys import argv

# Open the image
im = Image.open(argv[1])

# get the pixels from the image as a list of tuples and remove trailing black pixels
pixels = [tup for tup in list(im.getdata()) if tup != (0, 0, 0, 0)]

# convert the RGBA values to hex values
hex_array = []
for rgb_tuple in pixels:
    hex_string = ''
    for value in rgb_tuple:
        hex_string += hex(value)[2:].zfill(2)
    hex_array.append(hex_string)

# remove FF (the alpha channel) from the end
# of all strings in hex_array and concatenate into one string
hex_bytes_string = ''.join([string[:-2] for string in hex_array])

decoded_string = bytes.fromhex(hex_bytes_string).decode("ascii")

print(decoded_string)
