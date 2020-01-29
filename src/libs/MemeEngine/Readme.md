NAME

    libs.MemeEngine

PACKAGE CONTENTS

    MemeGenerator



## class MemeEngine(builtins.object)
       MemeEngine(output_dir)
       
       MemeEngine class to create a captionized image.
       
       Methods defined here:
       
       __init__(self, output_dir)
           Initialize self.  
       
       make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str
           Creates your own Meme
           :param img_path: image path
           :param text: body of the quote
           :param author: author of the quote
           :param width:  final width of image
           :return: meme image path
       
       
       
### Example of MemeEngine

```python
body  = "Sleep like its the end"
author = 'Anon'
img_path = './_data/dog/xander_1.jpg'
meme = MemeEngine('./tmp/')
path = meme.make_meme(img_path,body, author)
```