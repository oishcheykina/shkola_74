from django.db import models
from django.urls import reverse


#maktab

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("more", kwargs={"slug": self.slug})
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='teachers_photo/')
    field = models.CharField(max_length=300)
    phone_number = models.CharField(blank= True, null = True, max_length=250)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    
class Lavozim_Majburiyatlari(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Tarkibiy_Tuzilma(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Maktab_Nizomi(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Maktab_Madhiyasi(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Qubul_Kunlari(models.Model):
    date = models.DateTimeField(auto_now=True)
    day = models.CharField(max_length=150)
    time = models.CharField(max_length=150)
    lunch = models.CharField(max_length=150)
    def __str__(self):
        return self.day
    
class Ish(models.Model):
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    conclusion = models.CharField(max_length=150)
    
    def __str__(self):
        return self.conclusion
    
class Yil_Dasturi(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
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

    
class Imtihon_Materiallari(models.Model):
    year = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.year
    
    
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
    
    
    
class Administrators(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='admin_photo/')
    field = models.CharField(max_length=255)
    
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
    
#matbubot hizmati

class Announcement(models.Model):
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("announcement", kwargs={"slug": self.slug})
    
class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photo_gallery/')
    created_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("more_photo", kwargs={"photo_id": self.id})
    
class Davlat_Dasturlari(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("davlat_dasturi", kwargs={"slug": self.slug})
    
class Prezident_Qarori(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Xalq_Talim(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
#davlat ramzlari

class Gerb(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Gimn(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Flag(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Activist(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='teachers_photo/')
    field = models.CharField(max_length=300)
    grade = models.CharField(blank= True, null = True, max_length=250)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name