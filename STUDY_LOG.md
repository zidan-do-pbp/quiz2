# STUDY_LOG: quiz2

Catatan kerja. Tiap fase: apa yang dibuat, asumsi yang kita ambil, dan apa yang masih terbuka.

## Asumsi (tidak ada di notes, kita putuskan sendiri)
- (diisi per fase)

## Terbuka / perlu diverifikasi
- format timestamp cookie last_login
- nilai login_url (path atau nama route)
- definisi is_owner / is_editor
- id elemen DOM (result-count, pesan kosong)
- header CSRF + encoding body (B4)
- key payload JSON (B3)

## Log
- 2026-10-06 fase 0: repo masih kerangka kosong, env OK (Python 3.12.8, Django 5.2.18). Branch belajar sudah ada, dipakai.
- 2026-10-06 fase 1a: 'main' belum ada di INSTALLED_APPS, ditambahkan. main/urls.py dibuat (app_name='main'; route: home, register, login, logout).
- Asumsi fase 1: template flat di main/templates/ (tanpa prefix main/). Nama route 'main:login' dari ucapan "main login" (INF). Template tanpa font/CDN eksternal karena jaringan lab dibatasi. redirect pakai 'main:home' (redirect(home) tanpa nama gagal bila app_name diisi).
- 2026-10-06 fase 2a: kerangka A2 dibuat (Project, ProjectForm, 5 view stub, 5 route, 2 template, migrasi 0001, group Owner/Editor).
- Asumsi fase 2: field Project = name, description, owner (FK), starred_by (M2M), created_at. Owner = create/edit/delete; Editor = edit saja; semua user login boleh star. Semuanya keputusan kita, bukan dari notes (is_owner/is_editor tetap # VERIFY). login_url sengaja belum diisi (TODO, dibahas fase 3).