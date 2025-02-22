import imageio.v3 as iio

# filenames = [
#     'images/dino1.png',
#     'images/dino2.png',
#     'images/dino3.png',
#     'images/dino4.png'
# ]


# filenames = [
#     'images/hippocorn1.png',
#     'images/hippocorn2.png',
#     'images/hippocorn3.png',
#     'images/hippocorn4.png'
# ] 

filenames = [
    'images/chicklet1.png',
    'images/chicklet2.png',
    'images/chicklet3.png',
    'images/chicklet4.png'
]
print("Starting to load images")
images = [] 



for filename in filenames:
  print(f"Loading {filename}...") 
  images.append(iio.imread(filename)) 

print("All images loaded! Creating GIF...")
iio.imwrite('chicklet.gif', images, duration = 300, loop = 0)

print("GIF successfully created!")