from django.db import models
# Create your models here
import os
import sys
from . import SQL_Database
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from . import OCR_to_String
from . import SQL_Database
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='orc_ori_image/')
    info = SQL_Database.select()

    def __str__(self):
        info = SQL_Database.select()
        OCR_to_String.run()
        return self.title

class uploadPost(models.Model):
    imagesname = models.TextField()
    findimages = models.ImageField(upload_to='uploadimages/')

    def __str__(self):
        return self.imagesname