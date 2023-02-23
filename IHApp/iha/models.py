from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=False, unique=True,db_index=True)

    def __str__(self):
        return f"{self.name}"

class IhaModel(models.Model):
    marka = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    tarih = models.DateField(auto_now=True) #kayıtların eklenme tarihi otomatik gelsin.
    haberlesme_menzili = models.CharField(max_length=30)
    image = models.ImageField(upload_to= "images", blank=False,default="")
    agirlik = models.CharField(max_length=15)
    maks_hiz = models.CharField(max_length=15)
    havada_kalis = models.CharField(max_length=15)
    kanat_acikligi = models.CharField(max_length=15)
    uzunluk = models.CharField(max_length=15)
    slug = models.SlugField(blank=True, unique=True, db_index=True) #iha-kesif, iha-taaruz vs.
    categories = models.ManyToManyField(Category) #bir iha hem keşif hemde taaruz için kullanılabilir.(Bayraktar-akinci)

    def __str__(self):
        return f"{self.marka} {self.tarih}"


class Slider(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images")
    is_active = models.BooleanField(default=False)
    iha = models.ForeignKey(IhaModel, on_delete=models.SET_NULL, null=True, blank=True)