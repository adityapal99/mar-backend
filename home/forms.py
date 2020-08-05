from django import forms
from core.models import Catagories

departments = {
    'IT': 'Information Technology (IT)',
    'CSE': 'Computer Science (CSE)',
    'BME': 'Bio-medical Engineering (BME)',
    'EE': 'Electrical Engineering (EE)',
    'ECE': 'Electronics and Mass Communication Engineering (ECE)',
    'CE': 'Civil Engineering (CE)',
    'ME': 'Mechanical Engineering (ME)',
    'BCA': 'Bachelors in Computer Application (BCA)'
}

class SignUp(forms.Form):
    name = forms.CharField(max_length=200, label="Name", widget=forms.TextInput(attrs={"placeholder": "John Smith", "class": "form-control", "autocomplete": "off"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"placeholder": "john.smith@gmail.com", "class": "form-control", "autocomplete": "off"}))
    roll = forms.CharField(label="University Roll", widget=forms.TextInput(attrs={"placeholder": "123180704004", "class": "form-control", "autocomplete": "off"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "off"}), label="Password")

class LoginStudent(forms.Form):
    semail = forms.CharField(label="E-Mail", widget=forms.TextInput(attrs={"placeholder": "john@gmail.com", "class": "form-control", "autocomplete": "off"}))
    spassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "off", 'placeholder': '●●●●●●●●●●'}), label="Password")

class LoginTeacher(forms.Form):
    temail = forms.CharField(label="E-Mail", widget=forms.TextInput(attrs={"placeholder": "john@gmail.com", "class": "form-control", "autocomplete": "off"}))
    tpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "off", 'placeholder': '●●●●●●●●●●'}), label="Password")

class InsertData(forms.Form):
    link_to_file = forms.CharField(label="Link to Proof", widget=forms.TextInput(attrs={"placeholder": "Insert the link to document", 'class': "form-control", "autocomplete": "off"}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={"placeholder": "Describe your achivement", 'class': "md-textarea form-control", "autocomplete": "off", 'rows': '4'}))
    catagory = forms.ChoiceField(label="", choices=Catagories.objects.values_list('id', 'catName'), widget=forms.Select(attrs={'class': "browser-default custom-select custom-select-sass"}))

class StudentProfile(forms.Form):
    fname = forms.CharField(label="Name", widget=forms.TextInput(attrs={"placeholder": "John Smith", "class": "form-control", "autocomplete": "off"}))
    email = forms.CharField(label="E-Mail", widget=forms.TextInput(attrs={"placeholder": "john@gmail.com", "class": "form-control", "autocomplete": "off"}))
    roll = forms.CharField(label="University Roll", widget=forms.TextInput(attrs={"placeholder": "123180000000", "class": "form-control", "autocomplete": "off"}))
    collegeID = forms.CharField(label="College ID", widget=forms.TextInput(attrs={"placeholder": "JIS/20XX/XXXX", "class": "form-control", "autocomplete": "off"}))
    dept = forms.ChoiceField(label="Department", choices=departments.items())
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={"placeholder": "●●●●●●●●●●●", "class": "form-control", "autocomplete": "off"}))
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder": "●●●●●●●●●●●", "class": "form-control", "autocomplete": "off"}))


