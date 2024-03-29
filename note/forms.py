from django import forms

from note.models import Note, TechTag, NoteGroup


class NoteForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=TechTag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Note
        fields = ("title", "body", "tags", "resources",)


class NoteGroupForm(forms.ModelForm):
    notes = forms.ModelMultipleChoiceField(
        queryset=Note.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = NoteGroup
        fields = ("name", "notes", "tag",)


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
