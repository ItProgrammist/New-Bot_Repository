import os
import requests
import glob
from PIL import Image, ImageDraw, ImageFont


imgs = {
    "vs_bg": "./img/vs_bg.jpg",
    "vs_bg_animated": "./img/vs_bg_animated/frame_*.jpg"
}

# os.path.join(ПУТЬ ОТНОСИТЕЛЬНО main.py)
async def vs_create(url1: str, url2: str):
    #Основа vs_screen
    vs_bg = Image.open(os.path.join(imgs["vs_bg"]))

    # Размер аватаров
    size = (150, 150)

    # Скачиваем аватар по url
    f1 = Image.open( requests.get(url1, stream = True).raw).resize(size)
    f2 = Image.open( requests.get(url2, stream = True).raw).resize(size)

    # Определяем позицию для аватаров
    pos1 = (vs_bg.width//2 - f1.width*2, vs_bg.height//2 - f1.height//2)
    pos2 = (vs_bg.width//2 + f2.width, vs_bg.height//2 - f2.height//2)

    vs_bg.paste(f1, pos1)
    vs_bg.paste(f2, pos2)

    # сохранили изображение result.png
    vs_bg.save(os.path.join("./img", "result.png"))







# !!!АНИМИРОВАННЫЙ БОЙ!!! 
async def vs_create_animated(url1:str, url2:str, r1: str, r2: str):
    # Тернарный for
    # ЧТО_ДЕЛАЕМ for ИТЕРАТОР in СПИСОК
    vs_bg, *img = [Image.open(path) for path in glob.glob(imgs["vs_bg_animated"])]

    # vs_bg.resize(bg_size)

    # Размер аватаров
    size = (150, 150)

    # Скачиваем аватар по url
    f1 = Image.open( requests.get(url1, stream = True).raw).resize(size)
    f2 = Image.open( requests.get(url2, stream = True).raw).resize(size)

    # Определяем позицию для аватаров
    pos1 = (vs_bg.width//3 - f1.width, vs_bg.height//3 - f1.height//2)
    pos2 = (vs_bg.width//3 + f2.width  + 20, vs_bg.height//2 - f2.height//3)

    vs_bg.paste(f1, pos1)
    vs_bg.paste(f2, pos2)
    

    for im in img:
        im.paste(f1, pos1)
        im.paste(f2, pos2)
        fontsize = 28
        font = ImageFont.truetype("arial.ttf", fontsize)
        draw_text = ImageDraw.Draw(im)

        draw_text.text((vs_bg.width//3 - f1.width, vs_bg.height//3 - f1.height//2 + f1.height),r1,font=font,fill=('#696969'))
        draw_text.text((vs_bg.width//3 + f2.width  - 40, vs_bg.height//2 - f2.height//5 + f2.height-20),r2,font=font,fill=('#696969'))

    # "out.gif", save_all=True, append_images=[im2, im3], duration=100, loop=0
    vs_bg.save(fp=os.path.join("./img/result.gif"), append_images=img, save_all=True, duration=20, loop=0)





