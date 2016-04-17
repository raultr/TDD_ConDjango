from django.shortcuts import redirect,render
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text']) # Lo crea sin necesidad de llamar a guardar
		return redirect('/')
	
	items = Item.objects.all()
	#if request.method == 'POST':
	return render(request, 'home.html', {'items': items,})
	#return render(request,'home.html')