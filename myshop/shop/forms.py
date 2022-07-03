from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    CHOICES = (
        ('Казахстан','Казахстан'),
        ('Украина','Украина'),
        ('Белорусь','Белорусь'),
        ('Россия','Россия'),
        )
    username = forms.CharField(max_length = 30 ,
        label = 'Логин', 
        required=True,
        error_messages={'required' : 'Данное поле опязательно' , 'valid' : 'Введите правильный логин'})
    first_name = forms.CharField(max_length=30,label = 'Имя',
        required=True,
        error_messages={'required' : 'Данное поле опязательно'})
    last_name = forms.CharField(max_length=30,
        label = 'Фамилия',
        required=True,
        error_messages={'required' : 'Данное поле опязательно'})
    email = forms.EmailField(max_length=254,
        label = 'Электронная почта',
        required=True,
        error_messages={'required' : 'Данное поле опязательно'})
    password1 = forms.CharField(label = 'Пароль',
        required=True,
        error_messages={'required' : 'Данное поле опязательно'})
    password2 = forms.CharField(label = 'Подтвердите пароль',
        required=True,
        error_messages={'required' : 'Данное поле опязательно'})
    country = forms.ChoiceField(label = 'Выберите страну',
        choices = CHOICES,
        required=True,
        error_messages={'required' : 'Данное поле опязательно'})


    class Meta:
        model = User
        fields = ['username', 'first_name' ,'last_name','email', 'password1', 'password2','country']

class RegistrationForm(forms.ModelForm):
    CHOICES = (
    	('Казахстан'),
    	('Украина'),
    	('Белорусь'),
    	('Россия'),
    	)
    first_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget = forms.PasswordInput)
    country = forms.ChoiceField(choices = CHOICES)



    def __init__(self, *args, **kwargs):
        super().__init__(args, **kwargs)
        self.fields['first_name'].label='Имя'
        self.fields['email'].label='Электронная почта'
        self.fields['password'].label='Пароль'
        self.fields['country'].label='Страна'

    def clean_email(self):
    	email = self.cleaned_data['email']
    	if User.objects.filter(email = email).exists():
    		raise forms.ValidationError(f'Данный почтовый адрес уже зарегистрирован')


    class Meta:
        model = User
        fields = ('first_name', 'email', 'password','country', )