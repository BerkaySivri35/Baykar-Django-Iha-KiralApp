from django.shortcuts import redirect, render, get_object_or_404
from .models import IhaModel,Category,Slider
from iha.forms import IhaCreateForm
from django.contrib.messages import constants as messages
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.

def index(request):
    ihas = IhaModel.objects.all()
    categories = Category.objects.all()
    sliders = Slider.objects.filter(is_active = True)

    context ={
        'ihas': ihas,
        'categories': categories,
        'sliders':sliders
    }
    return render(request, 'iha/index.html',context)

def isAdmin(user):
    return user.is_superuser
#Auth Decorators ile admin olmayan kullanıcıların yetkisini kısıtlama.    

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q=request.GET["q"]
        ihas = IhaModel.objects.filter(model__icontains =q)
        categories = Category.objects.all()
    else:
        return redirect("/iha")
    
    context = {
        'categories': categories,
        'ihas': ihas,
        
    }
    return render(request, 'iha/search.html',context)
    
@login_required
def details(request, slug):
    ihas = get_object_or_404(IhaModel,slug = slug)
    context = {
        'ihas':ihas
    }
    return render(request, 'iha/iha-details.html',context)


def getIhasByCategory(request, slug):
    ihas = IhaModel.objects.filter(categories__slug = slug).order_by("tarih")
    categories = Category.objects.all()

    context ={
        'ihas':ihas,
        'categories':categories,
        'selectedCategory':slug
    }
    return render(request,'iha/list.html', context)


@user_passes_test(isAdmin)
def iha_list(request):
    ihas = IhaModel.objects.all()
    context ={
        'ihas':ihas,
    }
    return render(request, 'iha/iha-list.html', context)



def iha_edit(request,id):
    iha = get_object_or_404(IhaModel, pk=id)
    if request.method == 'POST':
        form = IhaCreateForm(request.POST, request.FILES, instance=iha)
        #kullanıcının girdiği bilgiler ile veri tabanında ki bilgiler karşılaştırılır.
        
        form.save()
        return redirect('iha_list')
        
        
    else:
        
        form = IhaCreateForm(instance = iha)
    return render(request,"iha/iha-edit.html",{"form":form})


def iha_delete(request,id):
    iha = get_object_or_404(IhaModel, pk=id)
    if request.method == 'POST':
        iha.delete()
        return redirect('iha_list')

    return render(request,'iha/iha-delete.html', {'iha':iha})


@user_passes_test(isAdmin)
def create_iha(request):
    if request.method == 'POST':
        form = IhaCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IhaCreateForm()
    return render(request,'iha/iha-kayit.html',{"form":form})