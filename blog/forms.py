from django import forms


class ParserForm(forms.ModelForm):
    url = forms.URLInput()

    class Meta:
        fields = (
            "url",
        )



