from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


#maktab

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория кружков'
        verbose_name_plural = 'Категории кружков'
    
class Post(models.Model):
    image = models.ImageField(upload_to='post_images/')
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("more", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сохраняем новый пост

        # Проверяем количество постов
        if Post.objects.count() > 100:
            oldest = Post.objects.order_by('created_at').first()  # Самый старый пост
            if oldest:
                oldest.delete()
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='teachers_photo/')
    field = models.CharField(max_length=300)
    phone_number = models.CharField(blank= True, null = True, max_length=250)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
    
    
class Lavozim_Majburiyatlari(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Должностные обязанности'
        verbose_name_plural = 'Должностные обязанности'
    
class Tarkibiy_Tuzilma(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Структурная организация'
        verbose_name_plural = 'Структурная организация'
    
class Maktab_Nizomi(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Устав школы'
        verbose_name_plural = 'Устав школы'
    
class Maktab_Madhiyasi(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Гимн школы'
        verbose_name_plural = 'Гимн школы'
    
class Qubul_Kunlari(models.Model):
    date = models.DateTimeField(auto_now=True)
    day = models.CharField(max_length=150)
    time = models.CharField(max_length=150)
    lunch = models.CharField(max_length=150)
    def __str__(self):
        return self.day
    
    class Meta:
        verbose_name = 'Дни приема'
        verbose_name_plural = 'Дни приема'
    
class Ish(models.Model):
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    conclusion = models.CharField(max_length=150)
    
    def __str__(self):
        return self.conclusion
    
    class Meta:
        verbose_name = 'Свободные вакансии'
        verbose_name_plural = 'Свободные вакансии'
    
class Yil_Dasturi(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Программа года'
        verbose_name_plural = 'Программа года'
    
    
#oquvchilarga

class Qongiroqlar_Jadvali(models.Model):
    SHIFT_CHOICES = [
        ('I', 'Первая смена'),
        ('II', 'Вторая смена'),
    ]
    
    shift = models.CharField(max_length=2, choices=SHIFT_CHOICES, verbose_name="Смена", null=True, blank=True)
    lesson_number = models.PositiveIntegerField(verbose_name="Номер урока", null=True, blank=True)
    start_time = models.TimeField(verbose_name="Начало урока", null=True, blank=True)
    end_time = models.TimeField(verbose_name="Конец урока", null=True, blank=True)
    break_duration = models.PositiveIntegerField(verbose_name="Перемена (мин)", default=5)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qoʻshilgan sana")  # Автоматическое добавление времени


    def __str__(self):
        return f"{self.get_shift_display()} - Урок {self.lesson_number}: {self.start_time} - {self.end_time}"
    
    class Meta:
        verbose_name = 'Расписание звонков'
        verbose_name_plural = 'Расписание звонков'

    
class Imtihon_Materiallari(models.Model):
    year = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.year
    
    class Meta:
        verbose_name = 'Экзаминационные материалы'
        verbose_name_plural = 'Экзаменационные материалы'
    
    
class Tugaraklar(models.Model):
    year = models.CharField(max_length=150, null=True, blank=True)
    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=255)
    count_of_pupils = models.CharField(max_length=200)
    days = models.TextField()
    time = models.TextField()
    teacher = models.CharField(max_length=255)
    category = models.ForeignKey('Category', blank='true', on_delete = models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Кружки'
        verbose_name_plural = 'Кружки'
    
    
    
class Administrators(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='admin_photo/')
    field = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Карусель Директор'
        verbose_name_plural = 'Карусель Директор'
    
class Principal(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='principal_photo/', null=True)
    phone_number = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    reception_days = models.TextField(null=True)
    date_of_birth = models.TextField(null=True)
    education = models.TextField(null=True)
    field = models.TextField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директор'
    
#matbubot hizmati

class Announcement(models.Model):
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("announcement", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сохраняем новый пост

        # Проверяем количество постов
        if Announcement.objects.count() > 100:
            oldest = Announcement.objects.order_by('created_at').first()  # Самый старый пост
            if oldest:
                oldest.delete()
    
class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photo_gallery/')
    created_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("more_photo", kwargs={"photo_id": self.id})
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото галерея'
    
class Davlat_Dasturlari(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("davlat_dasturi", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Государственная программа'
        verbose_name_plural = 'Государственные программы'
    
class Prezident_Qarori(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Указ президента'
        verbose_name_plural = 'Указы президента'
    
class Xalq_Talim(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Министерство образования'
        verbose_name_plural = 'Министерство образования'
    
#davlat ramzlari

class Gerb(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Герб'
        verbose_name_plural = 'Герб'
    
class Gimn(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Гимн'
        verbose_name_plural = 'Гимн'
    
class Flag(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Флаг'
        verbose_name_plural = 'Флаг'
    
class Activist(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='teachers_photo/')
    grade = models.CharField(blank= True, null = True, max_length=250)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Активист'
        verbose_name_plural = 'Активисты'
    
class Huquq_Majburiyatlar(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Права и обязанности'
        verbose_name_plural = 'Права и обязанности'
    
class Oquvchilarni_Qabul_Qilish(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Принятие учеников в школу'
        verbose_name_plural = 'Принятие учеников в школу'
        
class Main_Carousel(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    
    class Meta:
        verbose_name = 'Главная карусель'
        verbose_name_plural = 'Главная карусель'