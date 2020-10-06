# Generated by Django 3.1.2 on 2020-10-06 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('proteins', models.IntegerField(default=0)),
                ('fats', models.IntegerField(default=0)),
                ('carbonhydrates', models.IntegerField(default=0)),
                ('calories', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('last_login', models.DateTimeField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.users')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe2Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(choices=[('kg', 'Kg'), ('g', 'G'), ('l', 'L'), ('ml', 'Ml'), ('pcs', 'Pieces'), ('sp', 'Spoon'), ('tsp', 'Tea Spoon'), ('gls', 'Glass'), ('clove', 'Clove')], max_length=10)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.ingredients')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.recipes')),
            ],
        ),
    ]