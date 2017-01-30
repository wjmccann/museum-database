# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0005_auto_20170127_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=models.ImageField(blank=True, default='museum/static/museum/database/photo_not_available.png', upload_to='/home/coolamonrsl/museum-database/museum/static/museum/database/'),
        ),
        migrations.AlterField(
            model_name='collectionimage',
            name='image',
            field=models.ImageField(default='museum/static/museum/database/photo_not_available.png', upload_to='/home/coolamonrsl/museum-database/museum/static/museum/database/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='museum/static/museum/database/photo_not_available.png', upload_to='/home/coolamonrsl/museum-database/museum/static/museum/database/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('Art', (('Painting', 'Painting'), ('Drawing', 'Drawing'), ('Sculpture', 'Sculpture'), ('Poster', 'Poster'), ('Photograph', 'Photograph'))), ('Book', (('Book', 'Book'), ('Magazine', 'Magazine'), ('Journal', 'Journal'), ('Reference', 'Reference'), ('Comic', 'Comic'))), ('Diary', 'Diary'), ('Display', 'Display'), ('Equipment', (('Helmet', 'Helemet'), ('Binoculars', 'Binoculars'), ('Canteen', 'Canteen'), ('Bag', 'Bag'), ('Pack', 'Pack'), ('Webbing', 'Webbing'))), ('Weapon', (('Axe', 'Axe'), ('Grenade', 'Grenade'), ('Cannon', 'Cannon'), ('Knife', 'Knife'), ('Rifle', 'Rifle'), ('Pistol', 'Pistol'), ('Sword', 'Sword'), ('Dagger', 'Dagger'))), ('Flag', 'Flag'), ('Medal', 'Medal'), ('Model', (('Airplane', 'Airplane'), ('Helicopter', 'Helicopter'), ('Ship', 'Ship'), ('Submarine', 'Submarine'), ('Tank', 'Tank'), ('APC', 'APC'), ('Jeep', 'Jeep'))), ('Insignia', 'Insignia'), ('Plaque', 'Plaque'), ('Uniform', (('Boots', 'Boots'), ('Socks', 'Socks'), ('Trousers', 'Trousers'), ('Skirt', 'Skirt'), ('Shirt', 'Shirt'), ('Jacket', 'Jacket'), ('Tunic', 'Tunic'), ('Hat', 'Hat'), ('Belt', 'Belt'), ('Button', 'Button')))], max_length=20),
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(default='museum/static/museum/database/photo_not_available.png', upload_to='/home/coolamonrsl/museum-database/museum/static/museum/database/'),
        ),
    ]
