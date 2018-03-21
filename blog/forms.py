from django import forms

class UserRegistrationForm(forms.Form):
	username = forms.CharField(
		required = True,
		label = 'User Name',
		max_length = 32,
	)

	email = forms.CharField(
		required = True,
		label = 'E-mail',
		max_length = 32,
	)

	password = forms.CharField(
		required = True,
		label = 'Password',
		max_length = 32,
		widget = forms.PasswordInput()
	)