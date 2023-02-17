from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "name",
            "description"
        ]
    

                                     





# NON MODEL FORMS
# class TestForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()


#     def __init__(self, *args, **kwargs):
#         super().__init(*args, **kwargs)
#         self.fields['name'].widget.attrs.update({"class":"form-control"})
