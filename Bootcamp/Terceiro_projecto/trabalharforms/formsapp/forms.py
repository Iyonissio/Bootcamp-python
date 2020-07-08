from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validar(value):
    if value[0].lower() !='z':
        raise forms.ValidationError ("Nome deve iniciar com Z ")

class FormName(forms.Form):
    nome = forms.CharField(validators=[validar])
    email = forms.EmailField(label='your email',max_length=100)
    verify_email = forms.EmailField(label='verificar Email novamente:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validar])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Verifique se os Email inseridos sao iguais")