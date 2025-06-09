import numpy as np

def generate(volume_size_x, volume_size_y, volume_size_z, cube_size_x, cube_size_y, cube_size_z):
    volume = np.zeros((volume_size_x, volume_size_y, volume_size_z), dtype=np.uint8)
    start_x = int(volume_size_x / 2) - int(cube_size_x / 2)
    start_y = int(volume_size_y / 2) - int(cube_size_y / 2)
    start_z = int(volume_size_z / 2) - int(cube_size_z / 2)
    
    for x in range(start_x, start_x + cube_size_x):
        for y in range(start_y, start_y + cube_size_y):
            for z in range(start_z, start_z + cube_size_z):
                volume[x,y,z] = 255
    
    return volume