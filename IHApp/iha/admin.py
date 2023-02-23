from django.contrib import admin
from .models import IhaModel, Category, Slider
# Register your models here.

@admin.register(IhaModel)
class IhaAdmin(admin.ModelAdmin):
    list_display = ("marka","model","slug","category_list",)
    list_display_links = ("marka", "slug",)
    prepopulated_fields ={"slug":("model",),}
    search_fields = ("model",)

    def category_list(self,obj):
        html = ""
        for category in obj.categories.all():
            html += category.name + ", "
        return html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug",)
    prepopulated_fields ={"slug":("name",),}


admin.site.register(Slider)
