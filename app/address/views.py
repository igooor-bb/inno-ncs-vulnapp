from django.shortcuts import render

from .models import AddressModel
from .forms import SearchForm

def search_address(request):
    context = {}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['query']
            query = f"SELECT * FROM address_addressmodel WHERE address LIKE '%%{text}%%'"
            result = AddressModel.objects.raw(query)
            if result is not None and len(result) > 0:
                context['result'] = result
            else:
                context['not_found'] = True
    else:
        form = SearchForm()

    context['form'] = form
    return render(request, 'address/index.html', context)
