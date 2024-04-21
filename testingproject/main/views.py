from django.shortcuts import render, redirect
from django.contrib import messages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .config import EMAIL, PASSWORD, generate_unique_code
from .models import User, Collection, Link


# Create your views here.
def login(request):
    return render(request, 'main/login.html')

def reset(request):
    return render(request, 'main/reset_password_first.html')




def registration(request):
    return render(request, 'main/registration_first.html')
def confirm_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        sender_email = EMAIL
        receiver_email = email
        code = generate_unique_code()
        subject = 'SPECIAL CODE'
        message = f'special code: {code}'
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        # Отправка письма
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
    return render(request, 'main/registration.html')


def main(request):
    try:
        if request.method == 'POST':
            action = request.POST.get('action')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if action == 'registration':
                special_code = request.POST.get('code')
                name = request.POST.get('name')
                user_login = User(name = name, email = email, special_code = special_code, password = password)
                user_login.save()
                return render(request, 'main/main.html', {'user' : user_login})

            if action == 'login':
                user_login = User.objects.filter(email=str(email)).filter(password = str(password))
                if len(user_login)!=0:
                    return render(request, 'main/main.html', {'user' : str(user_login)})
                else:
                    return redirect('login', messages.error(request, 'Неправильный email или пароль.'))
                
            if action == 'reset':
                code = request.POST.get('code')
                user_login = User.objects.filter(email = str(email)).filter(special_code = str(code))
                if len(user_login)!=0:
                    User.objects.filter(email = str(email)).update(password=f'{password}')
                    return render(request, 'main/main.html', {'user' : str(user_login)})
                else:
                    return redirect('login', messages.error(request, 'Неправильный email или пароль.'))
    except:
        return redirect('login')
    return render(request, 'main/main.html')