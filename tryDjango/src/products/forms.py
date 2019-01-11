from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title       = forms.CharField(label='Title', 
		            widget=forms.TextInput(attrs={"placeholder": "Your title"}))
class Meta:
		model = Product
		fields = [
		    'title',
		  	'description',
		   	'price'
		]



class RawProductForm(forms.Form):
	title       = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	description = forms.CharField(
		required=False,
		 widget=forms.Textarea(
		 	attrs={
		 	"placeholder": "This is Description",
		 	"class": "new-class-name two",
		 	"id": "my-id-for-textarea",
		 	"rows": 20,
		 	"cols": 30
		} 
	 )
)
	price       = forms.DecimalField(initial=000.00, )