from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SectionForm
# Create your views here.


def index(request):
	form = SectionForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		week = form.cleaned_data.get('week')
		slide_link = form.cleaned_data.get('slide_link')
		date = form.cleaned_data.get('date')

		return HttpResponseRedirect('/')
	else:
		section_form = SectionForm()
		context = {
			'SectionForm': section_form
		}
		return render(request, 'index/index.html', context=context)