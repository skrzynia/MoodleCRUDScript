from django import forms
from django.forms import SelectDateWidget


class SectionForm(forms.Form):
	number_of_week = ((x,x) for x in range(1,28))
	week = forms.ChoiceField(choices=number_of_week)
	slide_link = forms.URLField()
	date = forms.DateField(
		widget=SelectDateWidget(
			empty_label="Provide Year, Month and Day of the workshops",
			years=(2020,2021)))