from PIL import Image
import random

im = Image.open("logo_ori.png")
pix = im.load()

flag = "treeCTF{hello_pixels_my_old_friend}"




row_start = 137
for c in flag:
  val = ord(c)
  i = 0
  while pix[row_start,i] == (255, 255, 255, 0):
    i += 1
  pix[row_start, i+1] = (255, 255, 255, val)
  row_start += 1
  print(row_start-1, i-1)

# put in some noise, so you can't just diff the images

for r in range(100):
    i = random.randint(0, 136)
    j = random.randint(0, im.size[1]-1)
    pix[i, j] = (255, 255, 255, pix[i,j][-1]+random.randint(-2, 2))

im.save("logo.png")