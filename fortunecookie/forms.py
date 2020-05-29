from django import forms 
from .models import FortuneCookie 


# creating a form 
class FortuneForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = FortuneCookie 
  
        # specify fields to be used 
        fields = [ 
            "fortune"] 