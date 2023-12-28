from PIL import Image


def imageRizer(image_path='', width=0,height=0):
    try:
        SIZE = width, height
        if image_path != '':
            image = Image.open(image_path)
            if (image.width > width) or (image.height > height):
                image.thumbnail(SIZE, Image.LANCZOS)
                image.save(image_path)
            return image
        
    except Exception as e:
        return str(e)
