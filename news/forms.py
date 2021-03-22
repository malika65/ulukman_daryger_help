from django import forms
from .models import Comments,PaymentsInfo,Gallery, ShowPhoto,Appeal
from django.forms import ModelForm, Textarea

from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _


class CommentsForm(forms.ModelForm):
    user_name = forms.CharField(label = '',max_length = 2000,
    required = True,widget = forms.TextInput(attrs = {
        'class': 'wrap-input100 validate-input input100',
        'placeholder': 'Ваше имя'}))

    user_email = forms.CharField(label = '',max_length = 2000,
    required = True,widget = forms.TextInput(attrs = {
        'class': 'wrap-input100 validate-input input100',
        'placeholder': 'E-mail'}))

    user_comment = forms.CharField(label = '',max_length = 12000,
    required = True,widget = forms.Textarea(attrs = {
        'class': 'wrap-input100 validate-input input100',
        'placeholder': 'Сообщение'}))

    class Meta:
        model = Comments
        fields = ('user_name', 'user_email','user_comment',)


class PaymentsInfoForm(forms.ModelForm):
    amount = forms.IntegerField(label = '',required = True,widget = forms.TextInput(attrs = {
        "onkeyup":"checkForm()",
        'id':'amount',
        'name':'amount',
        'type':'number' ,
        'class': 'form-field-6 form-control',
        'placeholder': 'Введите сумму для перевода'}))
    email = forms.CharField(label = '',max_length = 2000,required = True,widget = forms.TextInput(attrs = {
        "onkeyup":"checkForm()",
        'id':'email',
        'class': 'form-field-6 form-control',
        'placeholder': 'E-mail'}))

    class Meta:
        model = PaymentsInfo
        fields = ('amount', 'email',)

class SendEmailForm(forms.ModelForm):
    name = forms.CharField(label = '',max_length = 2000,required = True,widget = forms.TextInput(attrs = {
        'class': 'form-control',
        'placeholder': 'Name'}))
    email = forms.CharField(label = '',max_length = 2000,required = True,widget = forms.TextInput(attrs = {
        'class': 'form-control',
        'placeholder': 'Email'}))
    theme = forms.CharField(label = '',max_length = 2000,required = True,widget = forms.TextInput(attrs = {
        'class': 'form-control',
        'placeholder': 'Theme'}))
    comment = forms.CharField(label = '',max_length = 12000,required = True,widget = forms.Textarea(attrs = {
        'class': 'form-control',
        'placeholder': 'Message'}))

    class Meta:
        model = Appeal
        fields = ('name', 'email','theme','comment',)



class ShowAdminForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = (
            "name",
            "slug",
        )

    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, show):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            photo = ShowPhoto(show=show, photo=upload)
            photo.save()
