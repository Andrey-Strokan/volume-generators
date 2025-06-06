import numpy as np

def generate(volume_size, cube_size):
    volume = np.zeros((volume_size, volume_size, volume_size), dtype=np.uint8)
    start = int(volume_size / 2) - int(cube_size / 2)
    for x in range(start, start + cube_size):
        for y in range(start, start + cube_size):
            for z in range(start, start + cube_size):
                volume[x,y,z] = 255
    return volume