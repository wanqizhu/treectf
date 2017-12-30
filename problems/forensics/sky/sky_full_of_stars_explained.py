from shutil import copyfile
import numpy as np

copyfile("sky_original.jpg", "sky_map.jpg")
f = open("sky_map.jpg", "ab")
g = open("sky.txt", "r").read()
size = 1337


np.random.seed(ord(g[-1]))



sky = np.chararray((size, size))

sky[:] = '*'


# # field is a cartesian product of (0..size) X (0..size)
# # so all pairs (i, j) for 0 <= i, j < size
# field = np.zeros((size*size, 2))
# field[:, 0] = np.repeat(np.arange(size), size)
# field[:, 1] = np.tile(np.arange(size), size)
# # make it one-dimensional
# field2 = []
# for i in field:
# 	field2.append(tuple(i))

# print(field2)


# Nevermind, let's just pick random numbers encoded as    (x, y) = x * size + y

# generate random positions to put in the lyrics
positions = np.sort(np.random.choice(size*size, len(g), replace=False))


for i in range(len(g)):
	x = positions[i]
	y = x % size
	x //= size
	sky[x, y] = g[i]


f.write(sky)

#print(sky)

flag = "what'a'heavenly'view"
lyrics = g.split('\n')

h = open("sky_key.txt", "w")

for c in flag:
	possible_pos = []
	for i in range(len(lyrics)):
		line = np.asarray(list(lyrics[i]))
		if len(np.nonzero(line == c)[0]) > 0:
			possible_pos += [(i, j[0]) for j in np.nonzero(line == c)]

	#print(possible_pos)
	l = len(possible_pos)
	pos = possible_pos[np.random.randint(0, l)]
	h.write("%d %d\n" % (pos[0], pos[1]))
