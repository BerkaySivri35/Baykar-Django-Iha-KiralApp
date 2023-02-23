from django import forms
from iha.models import IhaModel
from django.forms import TextInput,FileInput,NumberInput,SelectMultiple
from django.utils.translation import gettext_lazy as _


class IhaCreateForm(forms.ModelForm):
    class Meta: # class MEta => alt class oluşturur.
        model = IhaModel
        fields = (
            'marka','model','haberlesme_menzili','image','agirlik','maks_hiz','havada_kalis','kanat_acikligi','uzunluk','categories','slug'
            )
        labels = {
            'marka':'Marka',
            'model':'Model',
            'haberlesme_menzili':'Haberleşme Menzili',
            'image':'Resim',
            'agirlik':'Ağırlık',
            'maks_hiz':'Maksimum Hız',
            'havada_kalis':'Havada Kalış Süresi',
            'kanat_acikligi':'Kanat Açıklığı',
            'uzunluk':'Uzunluk Bilgisi',
            'categories':'Hangi Kategoriye Ait ?',
            'slug':'Slug bilgisi'
        }

        widgets ={
            'marka':TextInput(attrs={"class":"form-control"}),
            'model':TextInput(attrs={"class":"form-control"}),
            'haberlesme_menzili':TextInput(attrs={"class":"form-control"}),
            'image':FileInput(attrs={'class':'form-control'}),
            'agirlik': TextInput(attrs={"class":"form-control"}),
            'maks_hiz':TextInput(attrs={"class":"form-control"}),
            'havada_kalis':TextInput(attrs={"class":"form-control"}),
            'kanat_acikligi':TextInput(attrs={"class":"form-control"}),
            'uzunluk':NumberInput(attrs={'class': 'form-control'}),
            'categories':SelectMultiple(attrs={"class":"form-control"}),
            'slug':TextInput(attrs={'class':'form-control'})
        }

        help_texts = {
            'slug': _('Ornek: taaruz'),
            'categories': _('Birden fazla seçim için (Ctrl + )')
        }


