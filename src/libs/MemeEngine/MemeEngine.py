from PIL import Image, ImageDraw, ImageFont
from random import randint


class MemeGenerator:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str:
        outputPath = self.output_dir + 'curr_meme.jpg'
        image = Image.open(img_path)
        image = image.crop((0, 0, width, width))
        font = ImageFont.truetype(font="./src/static/GrandHotel-Regular.otf", size=36)
        draw = ImageDraw.Draw(image, 'RGBA')
        random_x = randint(0, 100)
        random_y = randint(0, 400)
        draw.rectangle([random_x - 10, random_y - 5, random_x + len(text) * 20, random_y + 85], fill=(50, 50, 50, 125),
                       outline=(255, 255, 255))
        draw.text((random_x, random_y), text, (255, 255, 255), font=font)
        draw.text((random_x + 15, random_y + 35), '-' + author, (255, 255, 255), font=font)
        image.save(outputPath)
        return outputPath
