from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def draw_with_outline(text, font, draw, imgWidth, height_image, y_param):
    w, h = draw.textsize(text, font=font)
        
    x = (imgWidth - w) / 2
    y = int(y_param * height_image)
    
    outlineAmount = 3
    shadowColor = 'black'
    #create outline text
    for adj in range(outlineAmount):
        #move right
        draw.text((x-adj, y), text, font=font, fill=shadowColor)
        #move left
        draw.text((x+adj, y), text, font=font, fill=shadowColor)
        #move up
        draw.text((x, y+adj), text, font=font, fill=shadowColor)
        #move down
        draw.text((x, y-adj), text, font=font, fill=shadowColor)
        #diagnal left up
        draw.text((x-adj, y+adj), text, font=font, fill=shadowColor)
        #diagnal right up
        draw.text((x+adj, y+adj), text, font=font, fill=shadowColor)
        #diagnal left down
        draw.text((x-adj, y-adj), text, font=font, fill=shadowColor)
        #diagnal right down
        draw.text((x+adj, y-adj), text, font=font, fill=shadowColor)
    
    textColor = 'white'
    draw.text((x, y),text,font=font,
             fill=textColor)


def write_text_on_meme(source_img_path, output_img_path, text):
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont

    max_parts = 2

    if ';' in text:
        up_text, down_text = text.split(';')[:max_parts]
    else:
        up_text = ''
        down_text = text

    up_s = up_text.split()
    for i, (prev, current) in enumerate(zip(up_s, up_s[1:])):
        if prev == current:
            up_s.pop(i)
    up_text = ' '.join(up_s)

    down_s = down_text.split()
    for i, (prev, current) in enumerate(zip(up_s, up_s[1:])):
        if prev == current:
            down_s.pop(i)
    down_text = ' '.join(down_s)

    
    writeimg = Image.open(source_img_path)
    newimg = Image.new("RGB", writeimg.size)
    newimg.paste(writeimg)
    width_image = newimg.size[0]
    height_image = newimg.size[1]
    draw = ImageDraw.Draw(newimg)

    for font_size in range(50, 0, -1):
        font = ImageFont.truetype("impact.ttf", font_size)
        if font.getsize(up_text)[0] <= width_image:
            break
    else:
        print('no fonts fit!')

    imgWidth,imgHeight = writeimg.size
    txtWidth, txtHeight = draw.textsize(text, font=font)

    
    #### DRAW_UP
    draw_with_outline(up_text, font, draw, imgWidth, height_image, 0.05)
    
    for font_size in range(50, 0, -1):
        font = ImageFont.truetype("impact.ttf", font_size)
        if font.getsize(down_text)[0] <= width_image:
            break
    else:
        print('no fonts fit!')
        
    #### DRAW_DOWN
    draw_with_outline(down_text, font, draw, imgWidth, height_image, 0.85)
    
   

    newimg.save(output_img_path +".png")