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


# ---------------------------------------------------------------------------
# Fase 2 / A2 (notes C2): role dan CRUD Project
# ---------------------------------------------------------------------------
from django.contrib.auth.decorators import login_required  # noqa: E402
from django.http import HttpResponseForbidden  # noqa: E402
from django.shortcuts import get_object_or_404  # noqa: E402

from main.forms import ProjectForm  # noqa: E402
from main.models import Project  # noqa: E402


def is_owner(user):
    """# VERIFY: definisi is_owner TIDAK ada di notes, kita putuskan sendiri.

    TODO: return user.groups.filter(name='Owner').exists()
    """
    raise NotImplementedError('TODO: is_owner')


def is_editor(user):
    """# VERIFY: sama, definisi kita sendiri.

    TODO: return user.groups.filter(name='Editor').exists()
    """
    raise NotImplementedError('TODO: is_editor')


# TODO: pasang @login_required(login_url=...) di semua view di bawah.
#       # VERIFY: bentuk login_url (path '/login/' atau nama route 'main:login')


def project_list(request):
    """TODO:
    1. projects = Project.objects.select_related('owner').prefetch_related('starred_by')
       (prefetch supaya starred_by tidak N+1 query di template)
    2. render project_list.html dengan context:
       {'projects': projects, 'is_owner': is_owner(request.user),
        'is_editor': is_editor(request.user)}
    """
    raise NotImplementedError('TODO: project_list')


def project_create(request):
    """TODO:
    1. Izin DULU: bukan Owner -> return HttpResponseForbidden()  # 403
    2. form = ProjectForm(request.POST or None)
    3. POST + valid: obj = form.save(commit=False); obj.owner = request.user;
       obj.save(); redirect('main:project_list')
    4. Selain itu render project_form.html {'form': form, 'title': 'Buat project'}
    """
    raise NotImplementedError('TODO: project_create')


def project_edit(request, pk):
    """TODO:
    1. Izin DULU: bukan (Owner atau Editor) -> 403
    2. BARU project = get_object_or_404(Project, pk=pk)   # 404 kalau tidak ada
       (urutan ini yang ditanya kuis: 403 vs 404)
    3. form = ProjectForm(request.POST or None, instance=project)
    4. POST + valid: form.save(); redirect('main:project_list')
    5. Selain itu render project_form.html {'form': form, 'title': 'Edit project'}
    """
    raise NotImplementedError('TODO: project_edit')


def project_delete(request, pk):
    """TODO:
    1. Bukan POST -> HttpResponseNotAllowed(['POST'])  # 405
    2. Izin: bukan Owner -> 403
    3. project = get_object_or_404(Project, pk=pk); project.delete()
    4. redirect('main:project_list')
    """
    raise NotImplementedError('TODO: project_delete')


def toggle_star(request, pk):
    """TODO:
    1. Bukan POST -> 405
    2. project = get_object_or_404(Project, pk=pk)
    3. Kalau request.user sudah ada di project.starred_by: .remove(user), selain itu .add(user)
    4. redirect('main:project_list')
    """
    raise NotImplementedError('TODO: toggle_star')