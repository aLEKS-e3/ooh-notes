# Generated by Django 5.0.2 on 2024-03-04 13:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_rename_resource_note_resources'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'default_related_name': 'notes', 'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='note',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(to='note.techtag'),
        ),
        migrations.CreateModel(
            name='NoteGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.ManyToManyField(to='note.note')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='note.techtag')),
            ],
            options={
                'ordering': ['-created_at'],
                'default_related_name': 'note_groups',
            },
        ),
    ]
