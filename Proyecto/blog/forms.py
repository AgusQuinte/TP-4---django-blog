from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Tu nombre"}
        ),
    )
    body = forms.CharField(
        max_length=500,  # Límite de 500 caracteres
        widget=forms.Textarea(
            attrs={
                "class": "form-control", 
                "placeholder": "Deja tu comentario... (máximo 500 caracteres)",
                "maxlength": "500",  # Límite en el HTML también
                "rows": "6"
            }
        )
    )