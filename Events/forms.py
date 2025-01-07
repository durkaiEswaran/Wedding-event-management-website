from django import forms
from .models import BookingVenue, BookingCatering, BookingPhotography, BookingStageDecor,Contact,WeddingPackage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#register form
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BookingForm(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user name','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    user_email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user email','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user mobile no','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    class Meta:
        model = BookingVenue
        fields = ['user_name', 'user_email','mobile_no','booking_date']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'})
        }

class BookingFormCatering(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user name','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    user_email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user email','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user mobile no','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    class Meta:
        model = BookingCatering
        fields = ['user_name','user_email','mobile_no','booking_date']
        widgets = {
            'booking_date':forms.DateInput(attrs={'type':'date'})
        }

class BookingFormPhotography(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user name','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    user_email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user email','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user mobile no','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    class Meta:
        model = BookingPhotography
        fields = ['user_name','user_email','mobile_no','booking_date']
        widgets = {
            'booking_date':forms.DateInput(attrs={'type':'date'})
        }


class BookingFormStageDecor(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user name','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    user_email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user email','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user mobile no','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    class Meta:
        model = BookingStageDecor
        fields = ['user_name','user_email','mobile_no','booking_date']
        widgets = {
            'booking_date':forms.DateInput(attrs={'type':'date'})
        }
class BookingFormWeddingPackage(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user name','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    user_email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user email','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user mobile no','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    additional_services = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'user mobile no','style':'padding:3px;font-size:13px;margin:5px 0px;'}))
    class Meta:
        model = BookingStageDecor
        fields = ['user_name','user_email','mobile_no','additional_services','booking_date']
        widgets = {
            'booking_date':forms.DateInput(attrs={'type':'date'})
        }

class ContactForms(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':' First Name','style':'padding:3px;font-size:13px;'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':' Last Name','style':'padding:3px;font-size:13px;'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':' Email','style':'padding:3px;font-size:13px;'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':' Write your message here... ','style':'padding:3px;font-size:13px;'}))
    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','message']