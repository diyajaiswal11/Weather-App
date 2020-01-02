from django.forms import ModelForm, TextInput 
from .models import City 

#The Django Meta class is used to transfer information about the model 
# or other object to the Django framework; rather than using subclassing

class CityForm(ModelForm):
    class Meta:   #tells which model should be used to create this form
        model = City  
        fields=['name']   #which fields of form  
        #similar too input in html 
        widgets = {'name' : TextInput(attrs={'class' : 'input' , 'placeholder': 'City Name'})}

