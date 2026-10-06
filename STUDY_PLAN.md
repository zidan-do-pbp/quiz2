# STUDY_PLAN: Quiz 2 PBP (Django auth + JS)

Sumber: `notes-asistensi-django-auth-js.md` (rekaman asistensi 2026-10-04).
Letakkan file ini di root repo (`quiz2\STUDY_PLAN.md`). Centang fase yang sudah selesai.

## Titik awal (kondisi repo per 2026-10-06)

- `env` aktif, Python 3.12.8, Django 5.2.18, `manage.py check` bersih.
- Project: `quiz2_prep` (settings, urls). App: `main`.
- `main/views.py` dan `main/models.py` masih stub. `main/urls.py` belum ada.
- `quiz2_prep/urls.py` baru berisi `admin/`.
- Migrasi baru app bawaan. Belum ada model.

## Prinsip

1. Tiap fase = satu blok PowerShell yang membuat atau mengubah file, lalu satu commit git.
2. File dibuat sebagai **kerangka dengan TODO**. Kita isi bersama. Kunci jawaban ada di `_solutions\` (opsional).
3. Pakai tag dari notes: `[EXT]` dipercaya, `[INF]` dan `[AMB]` ditandai komentar `# VERIFY:` di kode.
4. Hal yang tidak ada di notes (nama field model, nama template, nama route) adalah **asumsi kita**, dan ditulis sebagai asumsi di `STUDY_LOG.md`.
5. Skrip tidak menimpa file yang sudah ada (pakai `Test-Path`). Aman dijalankan ulang.
6. Kalau spec kuis berbeda dari notes, spec kuis menang.

## Urutan fase

Prioritas kuis (dikonfirmasi dosen): JavaScript, halaman login + CSRF + kirim data ke DB, pembatasan halaman untuk user login. Karena itu fase 1, 3, dan 4-6 paling penting.

- [ ] **Fase 0: Persiapan.** Cek `INSTALLED_APPS` berisi `main`, cek `TEMPLATES`/`STATICFILES_DIRS`, buat branch `belajar`, buat `STUDY_LOG.md`. Tidak ada kode latihan.
- [ ] **Fase 1: A1 (C1) register, login, logout.**
  - File: `main/urls.py`, `main/views.py`, `main/templates/{base,home,register,login}.html`, `include` di `quiz2_prep/urls.py`.
  - Latihan: `UserCreationForm`, `AuthenticationForm`, `login()`, cookie `last_login` (+ `max_age`, `httponly`, `samesite`), logout POST-only (405) dan `delete_cookie`.
  - `# VERIFY:` format timestamp cookie, nama route login.
- [ ] **Fase 2: A2 (C2) role dan CRUD.**
  - File: `main/models.py` (`Project` dengan `starred_by`), `main/forms.py` (`ProjectForm`), view create/edit/delete/toggle_star, `project_list.html`, `project_form.html`, migrasi.
  - Latihan: `Group` Owner/Editor, 403 vs 405 vs 404, pengecekan izin sebelum fetch object, `prefetch_related('starred_by')`, `{% csrf_token %}`.
  - `# VERIFY:` definisi `is_owner`/`is_editor` (tidak ada di notes, kita putuskan sendiri).
- [ ] **Fase 3: A4 (C2) dashboard terlindungi.**
  - File: view `dashboard`, `dashboard.html`, skrip pembuat akun uji lewat `manage.py shell` (user biasa, Editor, Owner).
  - Latihan: `@login_required(login_url=...)`, menampilkan username.
  - `# VERIFY:` bentuk `login_url` (path atau nama route).
- [ ] **Fase 4: B1 (C3) `renderReports`.**
  - File: `main/templates/reports.html`, `main/static/js/reports.js` dengan array `reports` hardcoded.
  - Latihan: `innerHTML = ''`, `createElement`, `textContent` (bukan `innerHTML`), badge hilang/ditemukan, ringkasan hitungan, pesan kosong.
- [ ] **Fase 5: B2 (C3) filter dan modal.**
  - File: lanjutan `reports.js`.
  - Latihan: `applyFilters` (AND, `trim`, `toLowerCase`, `===`), `openModal`/`closeModal`, `init` yang mendaftarkan listener, jebakan `openModal` vs `openModal()`.
- [ ] **Fase 6: B3 (C4) `loadReports` (GET).**
  - File: model `Report`, endpoint JSON, seed data lewat shell, lanjutan `reports.js`.
  - Latihan: `fetch`, `async/await`, `response.ok`, `Array.isArray`, flag `isLoading`, `try/catch/finally`.
  - `# VERIFY:` key payload (`data.reports` atau array langsung).
- [ ] **Fase 7: B4 (C4) `submitReport` (POST + CSRF).**
  - File: endpoint POST, form di modal, lanjutan `reports.js`.
  - Latihan: event `submit` + `preventDefault`, validasi klien, CSRF, penanganan error per field (`__all__`), `isSubmitting = false` sebelum `closeModal()`, `finally` mengembalikan label tombol.
  - `# VERIFY:` nama header CSRF, encoding body.
- [ ] **Fase 8: Simulasi dan checklist lab.**
  - File: `QUIZ_DRILL.md` (soal latihan per komunitas, mengikuti "Suggested questions" di notes) dan checklist hari-H.
  - Isi checklist: pasang dependensi di venv lab lebih awal, favicon/Google Fonts yang error karena jaringan dibatasi (hapus baris `<link>` terkait), cek kursi/jaringan lab 1-2 hari sebelumnya.

## Cara kerja per fase (urutan yang sama tiap kali)

1. Aktifkan env:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned; & .\env\Scripts\Activate.ps1
   ```
2. Jalankan blok PowerShell fase tersebut (dari chat).
3. `python manage.py check`, lalu `python manage.py runserver` dan coba di browser.
4. Isi TODO. Kalau macet, tempel file dan error ke chat.
5. `git add -A; git commit -m "fase N: ..."`, lalu centang fase di atas.

## Prompt untuk melanjutkan di sesi baru

Tempel ini ke chat baru, beserta `notes-asistensi-django-auth-js.md` dan `STUDY_PLAN.md`:

> Saya sedang mengerjakan latihan quiz2 (repo github.com/zidan-do-pbp/quiz2, Windows PowerShell, env aktif di `...\PBP\quiz2`). Lanjutkan dari STUDY_PLAN.md. Fase terakhir yang selesai: [ISI]. Berikan blok PowerShell untuk fase berikutnya, jangan menimpa file yang sudah ada. Isi `main/views.py`, `main/urls.py`, dan `main/models.py` saat ini: [TEMPEL].

## Hal yang masih terbuka (dari notes)

- Format string timestamp cookie, nilai `login_url`, definisi `is_owner`/`is_editor`.
- ID elemen DOM (`result-count`, id pesan kosong), header CSRF dan encoding body, key payload JSON.
- Tanggal kuis pasti.
