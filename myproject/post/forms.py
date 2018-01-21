from django import forms
from django.core.exceptions import ValidationError


class CommentForm(forms.Form):
    postername=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Name*','required data-validation-required-message':'Please enter Your Name.'}),
        max_length=40,
        required=True,
        )
    description=forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','rows':'4','placeholder':'Write Comment*','required data-validation-required-message':'Cannot put blank comment.'}),
        required=True,
        max_length=300,
    )



    def __init__(self, *args, **kwargs):

        instance = kwargs.get('instance', None)

        kwargs.update(initial={
            # 'field': 'value'
        })

        super(CommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(CommentForm, self).clean()
        return self.cleaned_data
