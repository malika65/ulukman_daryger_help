# Generated by Django 3.1.5 on 2021-03-12 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, verbose_name='Имя пользователя')),
                ('user_email', models.EmailField(max_length=254, verbose_name='Email пользователя')),
                ('user_comment', models.TextField(max_length=1500, verbose_name='Комментарий пользователя')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='ForumInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Подзаголовок')),
                ('subtitle_ru', models.CharField(max_length=200, null=True, verbose_name='Подзаголовок')),
                ('subtitle_en', models.CharField(max_length=200, null=True, verbose_name='Подзаголовок')),
                ('subtitle_ky', models.CharField(max_length=200, null=True, verbose_name='Подзаголовок')),
                ('info', models.TextField(max_length=1500, verbose_name='Тело объявления')),
                ('info_ru', models.TextField(max_length=1500, null=True, verbose_name='Тело объявления')),
                ('info_en', models.TextField(max_length=1500, null=True, verbose_name='Тело объявления')),
                ('info_ky', models.TextField(max_length=1500, null=True, verbose_name='Тело объявления')),
                ('img_info', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название изображения')),
                ('slug', models.SlugField(max_length=1024)),
            ],
            options={
                'verbose_name': 'Галлерея',
                'verbose_name_plural': 'Галлерея',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('body', models.TextField(max_length=1500, verbose_name='Тело новости')),
                ('body_ru', models.TextField(max_length=1500, null=True, verbose_name='Тело новости')),
                ('body_en', models.TextField(max_length=1500, null=True, verbose_name='Тело новости')),
                ('body_ky', models.TextField(max_length=1500, null=True, verbose_name='Тело новости')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_paper', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('title_paper_ru', models.CharField(max_length=500, null=True, verbose_name='Заголовок')),
                ('title_paper_en', models.CharField(max_length=500, null=True, verbose_name='Заголовок')),
                ('title_paper_ky', models.CharField(max_length=500, null=True, verbose_name='Заголовок')),
                ('pdf', models.FileField(upload_to='media/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_created_ru', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_created_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_created_ky', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Газета',
                'verbose_name_plural': 'Газеты',
            },
        ),
        migrations.CreateModel(
            name='PaymentsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=200, verbose_name='Сумма')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('for_whom', models.CharField(blank=True, max_length=200, null=True, verbose_name='Кому')),
            ],
            options={
                'verbose_name': 'Перевод денег',
                'verbose_name_plural': 'Переводы денег',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя женщины')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Имя женщины')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Имя женщины')),
                ('name_ky', models.CharField(max_length=200, null=True, verbose_name='Имя женщины')),
                ('story', models.TextField(max_length=1500, verbose_name='История женщины')),
                ('story_ru', models.TextField(max_length=1500, null=True, verbose_name='История женщины')),
                ('story_en', models.TextField(max_length=1500, null=True, verbose_name='История женщины')),
                ('story_ky', models.TextField(max_length=1500, null=True, verbose_name='История женщины')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('elsom', models.CharField(blank=True, max_length=20, null=True, verbose_name='Элсом')),
                ('money_for_collecting', models.CharField(blank=True, max_length=50, null=True, verbose_name='Сумма к сбору')),
                ('date_created_women', models.DateTimeField(auto_now_add=True, null=True)),
                ('remaining_amount', models.CharField(blank=True, max_length=50, null=True, verbose_name='Оставшаяся сумма')),
                ('get_money', models.CharField(blank=True, max_length=50, null=True, verbose_name='Поступило')),
                ('gender', models.CharField(choices=[('1', 'Men'), ('2', 'Women'), ('3', 'Teenager')], max_length=300)),
            ],
            options={
                'verbose_name': 'Люди',
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.CreateModel(
            name='ShowPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Выберите изображение(-я)')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='news.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('news', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='news.news')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
