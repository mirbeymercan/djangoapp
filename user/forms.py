from django import forms

# ----- Kullanıcı Giriş -----
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')
    password = forms.CharField(min_length=6, max_length=24, label='Password', widget=forms.PasswordInput)


# ----- Kullanıcı Kayıt -----
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label = 'Username')
    password = forms.CharField(min_length=6, max_length=24, label='Password', widget = forms.PasswordInput)
    confirm = forms.CharField(min_length=6, max_length=24, label='Confirm Password', widget = forms.PasswordInput)
    
    # password == confirm olması lazım; if yerine clean methodu daha efektif

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise ValueError("Password informations must be same!")
        
        value = {
            'username': username,
            'password': password,
        }

        return value