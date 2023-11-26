# Generated by Django 4.2.7 on 2023-11-26 12:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='courses/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(upload_to='lessons/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='updated_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('subject', 'category')},
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('subject', 'course')},
        ),
        migrations.AddField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='lessons', to='courses.tag'),
        ),
    ]
