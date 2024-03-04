from django import forms

from note.models import Note, TechTag, NoteGroup


class NoteForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=TechTag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Note
        fields = "__all__"


class NoteGroupForm(forms.ModelForm):
    class Meta:
        model = NoteGroup
        fields = "__all__"
