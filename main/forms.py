from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, RadioSelect, FileInput, NumberInput
from django.contrib.auth.models import User
from .models import ApartmentImage, Profile, Apartment, StaticInput
from .models import Apartment, Profile

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True  # Разрешаем выбор нескольких файлов

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        if not data and initial:
            return initial
        return data

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

        widgets = {
            "username": TextInput(attrs={
                'class': 'enter-field-create',
                'placeholder': 'Ник'
            }),
            "password": PasswordInput(attrs={
                'class': 'enter-field-create',
                'placeholder': 'Пароль'
            }),
            "email": EmailInput(attrs={
                'class': 'enter-field-create',
                'placeholder': 'user@mail.com'
            }),
            "first_name": TextInput(attrs={
                'class': 'enter-field-create',
                'placeholder': 'Ваше имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'enter-field-create',
                'placeholder': 'Фамилия'
            }),
        }


class ApartmentForm(forms.Form):
    housenum = forms.CharField(min_length=1,
                               max_length=69,
                               widget=forms.TextInput({"class": "group-input",
                                                       "placeholder": "Номер дома"}
                                                      )
                               )
    name = forms.CharField(min_length=1,
                            max_length=69,
                           widget=forms.TextInput({"class": "group-input",
                                                   "placeholder": "Название"}
                                                  )
                               )
    stage = forms.CharField(min_length=1,
                            max_length=69,
                            widget=forms.TextInput({"class": "group-input",
                                                    "placeholder": "Этаж"}
                                                   )
                            )
    number = forms.CharField(min_length=1,
                             max_length=69,
                             widget=forms.TextInput({"class": "group-input",
                                                     "placeholder": "Номер квартиры"}
                                                    )
                             )
    city = forms.CharField(min_length=1,
                           max_length=69,
                           widget=forms.TextInput({"class": "group-input",
                                                   "placeholder": "Город"}
                                                  )
                           )
    street = forms.CharField(min_length=1,
                             max_length=69,
                             widget=forms.TextInput({"class": "group-input",
                                                     "placeholder": "Улица"}
                                                    )
                             )

    description = forms.CharField(min_length=1,
                                  max_length=300,
                                  widget=forms.Textarea({"class": "description"})
                                  )

    max_people = forms.DecimalField(widget=forms.NumberInput({"class": "count-input",
                                                              "placeholder":
                                                                  "Укажите максимальное количество постояльцев"
                                                              }
                                                             )
                                    )
    sleeping_places = forms.DecimalField(widget=forms.NumberInput({"class": "count-input",
                                                                   "placeholder": "Укажите количество спальных мест"}
                                                                  )
                                         )
    sleeping_rooms = forms.DecimalField(widget=forms.NumberInput({"class": "count-input",
                                                                  "placeholder": "Укажите число спален"}
                                                                 )
                                        )
    square = forms.DecimalField(widget=forms.NumberInput({"class": "count-input",
                                                                  "placeholder": "Укажите число спален"}
                                                                 )
                                        )
    bathrooms = forms.DecimalField(widget=forms.NumberInput({"class": "count-input",
                                                             "placeholder": "Укажите число ванных"}
                                                            )
                                   )

    cost_per_night = forms.DecimalField(widget=forms.NumberInput({"class": "group-input",
                                                                  "placeholder": "₽0"}
                                                                 )
                                        )
    prepayment = forms.DecimalField(widget=forms.NumberInput({"class": "group-input",
                                                              "placeholder": "₽0"}
                                                             )
                                    )
    min_nights = forms.DecimalField(widget=forms.NumberInput({"class": "count-input",
                                                              "placeholder": "Количество ночей"}
                                                             )
                                    )
    rent_type = forms.ChoiceField(choices=Apartment.RENT_TYPE_CHOICES,widget=forms.Select(attrs={
        'class': 'status-select'
        })
                                  )

class ImageForm(ModelForm):
    images = forms.FileField(
        widget=MultipleFileInput(attrs={'multiple': True}),
        required=False
    )

    class Meta:
        model = ApartmentImage
        fields = ['image']

class StaticInputForm(ModelForm):
    class Meta:
        model = StaticInput
        fields = ['water_hot_input', 'water_hot_payment','water_hot_receipt','water_cold_input',
                  'water_cold_receipt','water_cold_payment',
                  'electro_payment', 'electro_receipt', 'electro_input','gas_input',
                  'gas_payment','gas_receipt','GKX_payment',
                  'GKX_receipt','rent_payment','rent_receipt','water_hot_counter',
                  'water_cold_counter','electro_counter','gas_counter']

        widgets = {
            "water_hot_input": NumberInput(attrs={
                'class': 'desc-inp',
                'placeholder': 'Внесите показания счетчика (м³)'
            }),
            "water_hot_payment": NumberInput(attrs={
                'class': 'desc-inp',
                'placeholder': 'Внесите плату (₽)'
            }),
            "water_cold_input": NumberInput(attrs={
                'class': 'desc-inp',
                'placeholder': 'Внесите показания счетчика (м³)'
            }),
            "water_cold_payment": NumberInput(attrs={
                'class': 'desc-inp',
                'placeholder': 'Внесите плату (₽) '
            }),
            "electro_payment": NumberInput(attrs={
                'class': 'desc-inp',
                'placeholder': 'Внесите плату (₽)'
            }),
            "electro_input": NumberInput(attrs={
                'class': 'desc-inp',
                'placeholder': 'Внесите показания счетчика (кВТ * ч)'
            }),
            "gas_input": NumberInput(attrs={
                'class': 'desc-inp',
                'placeholder': 'Внесите показания счетчика (м³)'
            }),
            "gas_payment": NumberInput(attrs={
                'class': 'desc-inp',
                'placeholder': 'Внесите плату (₽)'
            }),
            "GKX_payment": NumberInput(attrs={
                'class': 'desc-inp',
                'placeholder': 'Внесите плату (₽)'
            }),
            "rent_payment": NumberInput(attrs={
                'class': 'desc-inp',
                'placeholder': 'Внесите плату (₽)'
            }),
            "water_cold_receipt": FileInput(attrs={
                'id':"water_receipt",
                'name':"photos",
                'style':"margin-top:10px;"
            }),
            "water_hot_receipt": FileInput(attrs={
                'id':"water_receipt",
                'name':"photos",
                'style':"margin-top:10px;"
            }),
            "electro_receipt": FileInput(attrs={
                'id':"electro_receipt",
                'name':"photos",
                'style':"margin-top:10px;"
            }),
            "gas_receipt": FileInput(attrs={
                'id':"gas_receipt",
                'name':"photos",
                'style':"margin-top:10px;"
            }),
            "GKX_receipt": FileInput(attrs={
                'id':"GKX_receipt",
                'name':"photos",
                'style':"margin-top:10px;"
            }),
            "rent_receipt": FileInput(attrs={
                'id':"rent_receipt",
                'name':"photos",
                'style':"margin-top:10px;",
            }),
            "water_hot_counter": FileInput(attrs={
                'id':"rent_receipt",
                'name':"photos",
                'style':"margin-top:10px;",
            }),
            "water_cold_counter": FileInput(attrs={
                'id':"rent_receipt",
                'name':"photos",
                'style':"margin-top:10px;",
            }),
            "electro_counter": FileInput(attrs={
                'id':"rent_receipt",
                'name':"photos",
                'style':"margin-top:10px;",
            }),
            "gas_counter": FileInput(attrs={
                'id':"rent_receipt",
                'name':"photos",
                'style':"margin-top:10px;",
            }),
        }



# class PhotoForm(forms.ModelForm):
#     class Meta:
#         model = Photo
#         fields = "__all__"
#         widgets = {
#             "image": forms.FileInput(attrs={"class": "...", "onchange": "preview(this)"})
#         }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
        widgets = {
            "avatar": forms.FileInput(attrs={
                'class': 'change-logo-text',
            }),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'info-input',
                'placeholder': 'Ваше имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'info-input',
                'placeholder': 'Ваша фамилия'
            }),
            "email": EmailInput(attrs={
                'class': 'info-input',
                'placeholder': 'user@mail.com'
            }),
        }


class PasswordUpdateForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'info-input'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'info-input'}))
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'info-input'}))
