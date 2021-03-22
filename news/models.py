from django.db import models
import datetime

class News(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    body = models.TextField(max_length=1500,verbose_name='Тело новости')
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    
    
    def __str__(self):
        return self.title

class Newspaper(models.Model):
    title_paper = models.CharField(max_length=500,verbose_name='Заголовок')
    pdf = models.FileField(upload_to = 'media/')
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    class Meta:
        verbose_name = 'Газета'
        verbose_name_plural = 'Газеты'
    
    
    def __str__(self):
        return self.title_paper

class NewsImage(models.Model):
    news = models.ForeignKey(News, default=None, on_delete=models.CASCADE,related_name='images')
    images = models.FileField(upload_to = 'images/')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return self.news.title


class People(models.Model):
    name = models.CharField(max_length=200,verbose_name='Имя')
    story = models.TextField(max_length=1500,verbose_name='История')
    pic = models.ImageField(null=True,blank=True)
    elsom = models.CharField(max_length=20,verbose_name='Элсом',null=True,blank=True)
    money_for_collecting = models.CharField(max_length=50,verbose_name='Сумма к сбору',null=True,blank=True)
    date_created_women = models.DateTimeField(auto_now_add=True,null=True)
    remaining_amount = models.CharField(max_length=50,verbose_name='Оставшаяся сумма',null=True,blank=True)
    get_money =  models.CharField(max_length=50,verbose_name='Поступило',null=True,blank=True)
    PEOPLE_CHOICES = [
        ('1', 'Men'),
        ('2', 'Women'),
        ('3', 'Teenager'),
    ]
    gender = models.CharField(max_length=300, choices = PEOPLE_CHOICES)


    class Meta:
        verbose_name = 'Люди'
        verbose_name_plural = 'Люди'


    def __str__(self):
        return self.name

class Comments(models.Model):
    user_name = models.CharField(max_length=200,verbose_name='Имя пользователя')
    user_email = models.EmailField(max_length=254,verbose_name='Email пользователя')
    user_comment = models.TextField(max_length=1500,verbose_name='Комментарий пользователя')


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.user_comment


class PaymentsInfo(models.Model):
    amount = models.CharField(max_length=200,verbose_name='Сумма')
    email = models.EmailField(max_length=254,verbose_name='Email')
    for_whom = models.CharField(max_length=200,verbose_name='Кому',null=True,blank=True)


    class Meta:
        verbose_name = 'Перевод денег'
        verbose_name_plural = 'Переводы денег'




    def __str__(self):
        return self.email



class ForumInfo(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    subtitle = models.CharField(max_length=200,verbose_name='Подзаголовок')
    info = models.TextField(max_length=1500,verbose_name='Тело объявления')
    img_info = models.ImageField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'




class Gallery(models.Model):
    name = models.CharField(max_length=64,verbose_name='Название изображения')
    slug = models.SlugField(max_length=1024)
  
    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'


class ShowPhoto(models.Model):
    show = models.ForeignKey(
        Gallery, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to='images/',verbose_name='Выберите изображение(-я)')

# Обращение
class Appeal(models.Model):
    name = models.CharField(max_length=200,verbose_name='Имя пользователя')
    email = models.EmailField(max_length=254,verbose_name='Email пользователя')
    theme = models.TextField(max_length=1500,verbose_name='Тема обращения')
    comment = models.TextField(max_length=1500,verbose_name='Обращение')


    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return self.name
        