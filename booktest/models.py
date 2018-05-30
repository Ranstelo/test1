from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length = 20)
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length = 20)
    hgender = models.BooleanField()
    hcomment = models.CharField(max_length = 128)
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname