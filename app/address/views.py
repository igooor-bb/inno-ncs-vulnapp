from django.shortcuts import render

from .models import AddressModel
from .forms import SearchForm

import bleach

def search_address(request):
    context = {}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['query']
            result = AddressModel.objects.filter(address__contains=text)
            if result is not None and len(result) > 0:
                address_list = [bleach.clean(x.address, strip=True) for x in result]
                context['result'] = address_list
            else:
                context['not_found'] = True
    else:
        form = SearchForm()

    context['form'] = form
    return render(request, 'address/index.html', context)
