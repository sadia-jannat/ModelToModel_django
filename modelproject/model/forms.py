import django
from django.contrib.auth import models
from django.core import validators
from django import forms
from django.forms import fields, widgets
from django import forms

#query for search
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)