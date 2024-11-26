from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from lab.models import Cars,Review,Game,Subscriptions,gadgets
from django.contrib.auth.decorators import login_required


def profile(request):
    return render(request, 'lab/profile.html', {'user': request.user})

def index(request):
    cars = Cars.objects.all()

    return render(request, 'lab/main.html', {'cars': cars, 'title': 'Главная страница'})
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('index')  # Редирект на главную страницу
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'lab/main.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} был создан!')
            return redirect('index')  # Редирект на главную страницу
    else:
        form = UserCreationForm()
    return render(request, 'lab/register.html', {'form': form})

def game(request):
    game = Game.objects.all()
    cars = Cars.objects.all()
    return render(request,'lab/game.html',{'games': game,'cars': cars,'title':'Игры' })
def gad(request):
    gad = gadgets.objects.all()
    cars = Cars.objects.all()
    return render(request,'lab/gadgets.html',{'gad': gad,'cars': cars,'title':'Гаджеты' })
def sub(request):
    sub = Subscriptions.objects.all()
    cars = Cars.objects.all()
    return render(request,'lab/Sub.html',{'sub': sub,'cars': cars,'title':'Гаджеты' })

def about(request):
    data = {
        'title': 'О нас',
        'about_text': (
            'Мы - компания, предоставляющая высококачественные услуги по аренде автомобилей. '
            'Наша цель - сделать ваше путешествие комфортным и незабываемым. '
            'Мы предлагаем широкий выбор автомобилей по доступным ценам. '
            'Наши клиенты - наша главная ценность.'
        ),
        'contact_info': {
            'address': 'г.Алматы, ул.Геодезическая 12',
            'phone': '+7 (123) 456-78-90',
            'email': 'al_bopov@mail.ru'
        },
        'map_embed_url': (
            'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d11626.736109537578!2d76.931354!3d43.237084'
            '!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38836eda7804dd07%3A0x719365a568e97946'
            '!2sSatbayev%20University!5e0!3m2!1sru!2skz!4v1696229639586!5m2!1sru!2skz'
        )
    }
    return render(request, 'lab/about.html', data)

def tar(request):
      # Получаем объект автомобиля по его ID
    return render(request,'lab/tarif.html',{'cars': cars,'title':'Тарифы' })
def ysl(request):
    return render(request,'lab/yslovia.html',{'title':'Условия' })

def kar(request):
    return render(request,'lab/kar.html',{'title':'Корзина' })

def cars(request, car_id):
    car = Cars.objects.all()
    cars = Cars.objects.get(id=car_id)  # Retrieve a Cars object using its ID
    return render(request, 'lab/car.html', {'cars': cars,'car':car,'title': 'Тарифы'})


def gads(request, gadget_id):
    car = Cars.objects.all()
    gadgets = Gadgets.objects.get(id=gadget_id)
    return render(request, 'lab/gadgetss.html', {'gadgets': gadgets,'car':car, 'title': 'Тарифы'})




def subs(request, sub_id):
    car = Cars.objects.all()
    subs = Subscriptions.objects.get(id=sub_id)
    return render(request, 'lab/subsss.html', {'sub': subs,'car':car, 'title': 'Тарифы'})

def games(request, game_id):
    car = Cars.objects.all()
    gam = Game.objects.get(id=game_id)


    return render(request, 'lab/gams.html', {'gam': gam,'car':car, 'title': 'Тарифы'})

def rev(request):
    reviews = Review.objects.all()
    return render(request, 'lab/rev.html', {'reviews': reviews, 'title': 'reviews'})









