from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.utils import timezone

# Fase 1 / A1 (notes C1). Di kuis, scope A1 = edit views.py saja.
# Tag: [EXT] dikatakan di rekaman, [INF] hasil perbaikan/pengisian, [AMB] tidak jelas.
# Aturan [EXT]: jangan simpan password/username/kredensial lain di cookie.


def home(request):
    # Disediakan, bukan bagian latihan.
    return render(request, 'home.html')


def register(request):
    """[EXT @03:08-@04:48] Method: GET + POST.

    TODO:
    1. form = UserCreationForm(request.POST or None)
    2. Kalau POST dan form.is_valid(): form.save(), lalu redirect ke route login.
       # VERIFY: 'main:login' hanya [INF] dari ucapan "main login"
    3. Selain itu: render register.html dengan {'form': form}
       (GET = form kosong; POST tidak valid = form + error, user tidak dibuat)
    """
    raise NotImplementedError('TODO: register')


def login_user(request):
    """[EXT @04:48-@07:08]

    TODO:
    1. form = AuthenticationForm(data=request.POST or None)
    2. POST + valid: login(request, form.get_user())
       response = redirect('main:home')
       response.set_cookie('last_login', <timestamp>)
       return response
       # VERIFY: format timestamp ikut spec tugas. Notes [AMB]: tahun-bulan-tanggal
       #         jam-menit-detik, pakai helper timezone (mis. timezone.now()).
    3. GET atau tidak valid: render login.html dengan {'form': form}
    Bonus (argumen set_cookie): max_age=3600, httponly=True, samesite='Lax'
    """
    raise NotImplementedError('TODO: login_user')


def logout_user(request):
    """[EXT @07:14-@08:23]

    TODO:
    1. Bukan POST: return HttpResponseNotAllowed(['POST'])  # 405, nama pasti [INF]
    2. POST: logout(request)
       response = redirect('main:home')
       response.delete_cookie('last_login')
       return response
       (cookie dihapus pada response yang sama dengan redirect)
    """
    raise NotImplementedError('TODO: logout_user')