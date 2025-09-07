from django import forms
from django.core.exceptions import ValidationError
from .models import Post





class PostForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['name', 'description', 'category', 'datepublic' , 'author_name']


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентичным названию."
            )

        return cleaned_data