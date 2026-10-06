from django import forms

from main.models import Project


class ProjectForm(forms.ModelForm):
    """Fase 2 / A2. Dipakai view create dan edit.

    TODO (opsional): tambah clean_name() yang menolak nama kosong setelah strip()
    TODO (opsional): widget Textarea(attrs={'rows': 4}) untuk description
    """

    class Meta:
        model = Project
        fields = ['name', 'description']