from django import forms
from .models import OliveOilCalculation

class OliveOilCalculationForm(forms.ModelForm):
    class Meta:
        model = OliveOilCalculation
        exclude = ['date_calculated']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[field].label
            })
