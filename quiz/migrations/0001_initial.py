# Generated by Django 4.2.1 on 2023-06-04 19:24

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
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='إسم القسم')),
                ('summary', models.CharField(max_length=1000, verbose_name='نبذه مختصره عن القسم')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pic_book', models.ImageField(blank=True, null=True, upload_to='Content/Content_image')),
                ('pdf_File', models.FileField(blank=True, null=True, upload_to='Content/Content_pdf')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.category', verbose_name='إسم القسم')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
