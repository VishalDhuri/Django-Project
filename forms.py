from django import forms
from .models import userr , Review , fooditem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Newuser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta :
        model = User
        fields = ("username","email","password1","password2")

class Createuser(forms.ModelForm):
    class Meta :
        model = userr
        fields = '__all__'

class CreateReview(forms.ModelForm):
    class Meta :
        model = Review
        fields = '__all__'

class Createfood(forms.ModelForm):
    class Meta :
        model = fooditem
        fields = '__all__'
