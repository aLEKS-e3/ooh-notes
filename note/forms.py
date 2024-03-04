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


class NoteSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"})
    )


class NoteGroupSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class TechTagFilterForm(forms.Form):
    tag = forms.ModelChoiceField(
        queryset=TechTag.objects.all(),
        widget=forms.RadioSelect,
        label="",
        required=False
    )
