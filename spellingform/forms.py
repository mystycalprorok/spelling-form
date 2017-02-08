"""
Forms
"""

from django import forms

class SpellingForm(forms.Form):
    number = forms.IntegerField(min_value=0)
