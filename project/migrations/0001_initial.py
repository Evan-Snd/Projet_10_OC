# Generated by Django 3.2.5 on 2022-09-15 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=8192)),
                ('type', models.CharField(choices=[('BackEnd', 'BackEnd'), ('FrontEnd', 'FrontEnd'), ('IOS', 'IOS'), ('Android', 'Android')], default='BackEnd', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=500)),
                ('tag', models.CharField(choices=[('Tâche', 'Tâche'), ('Bug', 'Bug'), ('Amélioration', 'Amélioration')], default='Tâche', max_length=20)),
                ('priority', models.CharField(choices=[('Faible', 'Faible'), ('Moyen', 'Moyen'), ('Elevé', 'Elevé')], default='Moyen', max_length=20)),
                ('status', models.CharField(choices=[('Début', 'Début'), ('En cours', 'En cours'), ('Terminé', 'Terminé')], default='En cours', max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Contributeur', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Auteur', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projects')),
            ],
            options={
                'verbose_name_plural': 'Issues',
            },
        ),
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('Responsable', 'Responsable'), ('Dev', 'Dev')], default='Dev', max_length=20)),
                ('role', models.CharField(blank=True, max_length=128)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contributors',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.issues')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
