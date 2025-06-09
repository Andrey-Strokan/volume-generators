import numpy as np
from PIL import Image, ImageDraw, ImageFont

def generate(volume_size_x, volume_size_y, volume_size_z):
    volume = np.zeros((volume_size_x, volume_size_y, volume_size_z), dtype=np.uint8)
    
    for z in range(volume_size_z):
        img = Image.new('L', (volume_size_x, volume_size_y), color=0)
        draw = ImageDraw.Draw(img)
        
        font_size = volume_size_x / 5.5
        font = ImageFont.truetype("arial.ttf", font_size)
        
        digit = f'z: {str(z)}'
        bbox = draw.textbbox((0, 0), digit, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = volume_size_x - text_width
        y = volume_size_y - text_height*1.5
        draw.text((x, y), digit, fill=255, font=font)
        
        digit_img = np.array(img)
        digit_img[digit_img > 0] = 255
        mask = (digit_img > 0)
        volume[:, :, z][mask] = digit_img[mask]

    for x in range(volume_size_x):
        img = Image.new('L', (volume_size_z, volume_size_y), color=0)
        draw = ImageDraw.Draw(img)
        
        font_size = volume_size_z / 5.5
        font = ImageFont.truetype("arial.ttf", font_size)
        
        digit =  f'x: {str(x)}'
        bbox = draw.textbbox((0, 0), digit, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        z = 0
        y = 0
        draw.text((z, y), digit, fill=255, font=font)
        
        digit_img = np.array(img)
        digit_img[digit_img > 0] = 255
        mask = (digit_img > 0)
        volume[x, :, :][mask] = digit_img[mask]

    for y in range(volume_size_y):
        img = Image.new('L', (volume_size_z, volume_size_x), color=0)
        draw = ImageDraw.Draw(img)
        
        font_size = volume_size_z / 5.5
        font = ImageFont.truetype("arial.ttf", font_size)
        
        digit =  f'y: {str(y)}'
        bbox = draw.textbbox((0, 0), digit, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = volume_size_z - text_width
        z = 0
        draw.text((z, x), digit, fill=255, font=font)
        
        digit_img = np.array(img)
        digit_img[digit_img > 0] = 255
        mask = (digit_img > 0)
        volume[:, y, :][mask] = digit_img[mask]
    
    return volume