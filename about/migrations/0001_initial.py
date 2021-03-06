# Generated by Django 2.2.12 on 2020-06-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images/siteinfo')),
                ('slogan', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('map_url', models.URLField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'site info',
                'verbose_name_plural': 'sites infos',
            },
        ),
        migrations.CreateModel(
            name='SocialCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('lien', models.URLField()),
                ('icone', models.CharField(choices=[('facebook', 'fa-facebook-f'), ('instagram', 'fa-instagram'), ('google-plus', 'fa-google-plus-g'), ('linkedin', 'fa-linkedin-in')], max_length=20)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'social account',
                'verbose_name_plural': 'socials account',
            },
        ),
    ]
