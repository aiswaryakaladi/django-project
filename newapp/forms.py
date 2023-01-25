from django import forms

class regform(forms.Form):
    name=forms.CharField(max_length=25)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)


class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)


class employeeform(forms.Form):
    name=forms.CharField(max_length=25)
    salary=forms.IntegerField()
    email=forms.EmailField()
    cname=forms.CharField(max_length=20)
    dname=forms.CharField(max_length=20)


class checkform(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()


class fileform(forms.Form):
    itemname=forms.CharField(max_length=20)
    image=forms.FileField()


class cardform(forms.Form):
    name=forms.CharField(max_length=20)
    price=forms.IntegerField()
    image=forms.FileField()
    description=forms.CharField(max_length=60)


class xamform(forms.Form):
    name = forms.CharField(max_length=20)
    image = forms.FileField()

