value = int(input("The colour value: "), 16)
red = (value & 0xFF0000) >> 16
green = (value & 0x00FF00) >> 8
blue = value & 0x0000FF

print("Red: {}, Green: {}, Blue: {}".format(red, green, blue))
