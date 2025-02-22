import imageio.v3 as iio

filenames = [
    'images/dino1.png',
    'images/dino2.png',
    'images/dino3.png',
    'images/dino4.png'
]

images = []

for filename in filenames:
    images.append(iio.iamread(filename))

iio.write('dino.gif', images, duration = 300, loop = 0)