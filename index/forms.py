from django import forms
from django.forms import SelectDateWidget


class SectionForm(forms.Form):
	number_of_week = ((x,x) for x in range(1,28))
	week = forms.ChoiceField(choices=number_of_week, label="Number of Section")
	slide_link = forms.URLField(label="Slide URL in format http://mikhail-cct.github.io/ooapp/wk2/#/: ",widget=forms.TextInput(attrs={'placeholder': 'url'}))
	date = forms.DateField(
		widget=SelectDateWidget(
			empty_label="Provide Year, Month and Day of the workshops",
			years=(2020,2021)),label="Date of lecture")