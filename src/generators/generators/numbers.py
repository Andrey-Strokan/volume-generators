import numpy as np
from PIL import Image, ImageDraw, ImageFont

def generate(volume_size):
    volume = np.zeros((volume_size, volume_size, volume_size), dtype=np.uint8)
    
    for z in range(volume_size):
        img = Image.new('L', (volume_size, volume_size), color=0)
        draw = ImageDraw.Draw(img)
        
        font_size = volume_size / 5.5
        font = ImageFont.truetype("arial.ttf", font_size)
        
        digit = f'z: {str(z)}'
        bbox = draw.textbbox((0, 0), digit, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = volume_size - text_width
        y = volume_size - text_height*1.5
        draw.text((x, y), digit, fill=255, font=font)
        
        digit_img = np.array(img)
        digit_img[digit_img > 0] = 255
        mask = (digit_img > 0)
        volume[:, :, z][mask] = digit_img[mask]

    for x in range(volume_size):
        img = Image.new('L', (volume_size, volume_size), color=0)
        draw = ImageDraw.Draw(img)
        
        font_size = volume_size / 5.5
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

    for y in range(volume_size):
        img = Image.new('L', (volume_size, volume_size), color=0)
        draw = ImageDraw.Draw(img)
        
        font_size = volume_size / 5.5
        font = ImageFont.truetype("arial.ttf", font_size)
        
        digit =  f'y: {str(y)}'
        bbox = draw.textbbox((0, 0), digit, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = volume_size - text_width
        z = 0
        draw.text((x, z), digit, fill=255, font=font)
        
        digit_img = np.array(img)
        digit_img[digit_img > 0] = 255
        mask = (digit_img > 0)
        volume[:, y, :][mask] = digit_img[mask]
    
    return volume