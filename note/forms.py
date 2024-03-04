from django import forms

from note.models import Note, TechTag


class NoteCreationForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=TechTag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Note
        fields = "__all__"
