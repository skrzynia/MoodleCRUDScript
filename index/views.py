from django.shortcuts import render
from django.http import HttpResponseRedirect
from SectionClass import SectionClass
from .forms import SectionForm
import HTMLCreator as creator
import PDFCreator as pdf
import MoodleCRUD as mc
from WebScrapper import getTitleAndHTML,getVideo
import re
from django.http import FileResponse, Http404
# Create your views here.


def index(request):
	form = SectionForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		week = form.cleaned_data.get('week')
		slide_link = form.cleaned_data.get('slide_link')
		date = form.cleaned_data.get('date')
		sc = SectionClass(week,slide_link,date)
		title,html = getTitleAndHTML(slide_link)
		creator.createHTML(week,sc.slideHTML)
		pdf.printToPdf(week,slide_link)
		mc.LocalUpdateSections("8",[{'section': week,'summary': creator.getHTMLTag(week,str(slide_link)) + getVideo(date) +pdf.getPDFTag(week), 'name': title}])


		return HttpResponseRedirect('/')
	else:
		section_form = SectionForm()
		context = {
			'SectionForm': section_form
		}
		return render(request, 'index/index.html', context=context)


def files(request, num):
	try:
		return FileResponse(open(pdf.getPDFName(num), 'rb'), content_type='application/pdf')
	except FileNotFoundError:
		raise Http404()




