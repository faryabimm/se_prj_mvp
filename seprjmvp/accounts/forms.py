from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True, help_text='required')
    email = forms.EmailField(max_length=254, required=True, help_text='required')
    # is_admin = forms.CheckboxInput(check_test=True)

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        # user.is_admin = self.cleaned_data["is_admin"]
        if commit:
            user.save()
        return user
