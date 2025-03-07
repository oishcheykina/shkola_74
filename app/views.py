from django.shortcuts import render,  get_object_or_404
from django.core.paginator import Paginator
from .models import *

def custom_page_not_found(request, exception):
    admins = Administrators.objects.all()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, "404.html", dic, status=404)


# Create your views here.
def home(request):
    admins = Administrators.objects.all()
    posts = Post.objects.all().order_by('-created_at')  
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    main_carousel = Main_Carousel.objects.all()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
        'main_carousel': main_carousel,
    }
    return render(request, 'index.html', dic)


def principal(request):
    admins = Administrators.objects.all()
    principall = Principal.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'principall': principall,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'maktab/maktab-direktori.html', dic)

def more(request, slug):
    admins = Administrators.objects.all()
    post = get_object_or_404(Post, slug=slug)
    viewed_news = request.session.get('viewed_news', [])

    if slug not in viewed_news:
        post.views += 1
        post.save(update_fields=['views'])
        viewed_news.append(slug)
        request.session['viewed_news'] = viewed_news
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'post': post,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'more.html', dic)

def school_team(request):
    admins = Administrators.objects.all()
    teachers = Teacher.objects.all()
    paginator = Paginator(teachers, 6)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.first()
    teacherr = Teacher.objects.first()
    dic = {
        'admins': admins,
        'yil_dasturi': yil_dasturi,
        'page_obj': page_obj,
        'teacherr': teacherr,
    }
    return render(request, 'maktab/maktab-jamoasi.html', dic)

def lavozim_majburiyatlari(request):
    admins = Administrators.objects.all()
    lavozim_majburiyatlari = Lavozim_Majburiyatlari.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'lavozim_majburiyatlari': lavozim_majburiyatlari,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'maktab/lavozim-majburiyatlari.html', dic)

def tarkibiy_tuzilma(request):
    admins = Administrators.objects.all()
    tarkibiy_tuzilma = Tarkibiy_Tuzilma.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'tarkibiy_tuzilma': tarkibiy_tuzilma,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'oqituvchilarga/tarkibiy-tuzilma.html', dic)

def maktab_nizomi(request):
    admins = Administrators.objects.all()
    maktab_nizomi = Maktab_Nizomi.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'maktab_nizomi': maktab_nizomi,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'maktab/maktab-nizomi.html', dic)

def maktab_madhiyasi(request):
    admins = Administrators.objects.all()
    maktab_madhiyasi = Maktab_Madhiyasi.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'maktab_madhiyasi': maktab_madhiyasi,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'maktab/maktab-madhiyasi.html', dic)

def qabul_kunlari(request):
    admins = Administrators.objects.all()
    qubul_kunlari = Qubul_Kunlari.objects.all()
    qubul_kun = Qubul_Kunlari.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'qabul_kunlari': qubul_kunlari,
        'yil_dasturi': yil_dasturi,
        'qabul_kun': qubul_kun,
    }
    return render(request, 'maktab/qabul-kunlari.html', dic)

def ish(request):
    admins = Administrators.objects.all()
    ish = Ish.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'ish': ish,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'oqituvchilarga/bosh-ish-orinlari.html', dic)
#oqituvchilarga

#oquvchilarga

def imtihon_materiallari(request):
    admins = Administrators.objects.all()
    imtihon_materiallari = Imtihon_Materiallari.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'imtihon_materiallari': imtihon_materiallari,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'oquvchilarga/imtihon-materiallari.html', dic)

def qongiroqlar(request):
    admins = Administrators.objects.all()
    first_shift = Qongiroqlar_Jadvali.objects.filter(shift='I').order_by('lesson_number')
    second_shift = Qongiroqlar_Jadvali.objects.filter(shift='II').order_by('lesson_number')
    yil_dasturi = Yil_Dasturi.objects.first()
    last_added = Qongiroqlar_Jadvali.objects.latest('created_at')  # Получаем последний добавленный объект
    last_added_date = last_added.created_at.strftime("%d-%m-%Y, %H:%M")
    dic = {
        'admins': admins,
        'yil_dasturi': yil_dasturi,
        'first_shift': first_shift,
        'second_shift': second_shift,
        'last_added_date': last_added_date,
    }
    return render(request, 'oquvchilarga/qongiroqlar-jadvali.html', dic)

def togaraklar_jadvali(request):
    admins = Administrators.objects.all()
    sport_category = Category.objects.get(name="Sport")
    sport_items_count = Tugaraklar.objects.filter(category=sport_category).count()
    togaraklar_jadvali = Tugaraklar.objects.all()
    fan_category = Category.objects.get(name="Fan")
    fan_items_count = Tugaraklar.objects.filter(category=fan_category).count()
    
    qiziqishlar_boyicha_togaraklar = Category.objects.get(name="Qiziqishlar bo‘yicha to‘garaklar")
    qiziqishlar_boyicha_togaraklar_items_count = Tugaraklar.objects.filter(category=qiziqishlar_boyicha_togaraklar).count()
    items_count = Tugaraklar.objects.all().count()
    yil_dasturi = Yil_Dasturi.objects.first()
    tugarakk = Tugaraklar.objects.first()
    dic = {
        'admins': admins,
        'togaraklar_jadvali': togaraklar_jadvali,
        'yil_dasturi': yil_dasturi,
        'sport_items_count': sport_items_count,
        'fan_items_count': fan_items_count,
        'qiziqishlar_boyicha_togaraklar_items_count': qiziqishlar_boyicha_togaraklar_items_count,
        'items_count': items_count,
        'tugarakk': tugarakk,  # Получаем первый добавленный объект
    }
    return render(request, 'oquvchilarga/togaraklar-jadvali.html', dic)

def huquq(request):
    admins = Administrators.objects.all()
    yil_dasturi = Yil_Dasturi.objects.first()
    huquq_majburiyatlar = Huquq_Majburiyatlar.objects.first()
    dic = {
        'admins': admins,
        'yil_dasturi': yil_dasturi,
        'huquq_majburiyatlar': huquq_majburiyatlar,
    }
    return render(request, 'ota-onalarga/huquq-va-majburiyatlar.html', dic)

def oquvchilarni_qabul_qilish(request):
    admins = Administrators.objects.all()
    yil_dasturi = Yil_Dasturi.objects.first()
    oquvchilarni_qabul_qilishh = Oquvchilarni_Qabul_Qilish.objects.first()
    dic = {
        'admins': admins,
        'yil_dasturi': yil_dasturi,
        'oquvchilarni_qabul_qilishh': oquvchilarni_qabul_qilishh,
    }
    return render(request, 'ota-onalarga/maktab-oquvchilarni-qabul-qilish.html', dic)


def news(request):
    admins = Administrators.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'matbuot-xizmati/yangiliklar.html', dic)

def announcements(request):
    admins = Administrators.objects.all()
    announcements = Announcement.objects.all().order_by('-created_at')
    paginator = Paginator(announcements, 6)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'matbuot-xizmati/elonlar.html', dic)

def foto_galery(request):
    admins = Administrators.objects.all()
    photos = Photo.objects.all().order_by('-created_at')
    paginator = Paginator(photos, 6)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.first()
    post = Photo.objects.first()
    dic = {
        'admins': admins,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
        'post': post,
    }
    return render(request, 'matbuot-xizmati/foto-galereya.html', dic)

def davlat_dasturlari(request):
    admins = Administrators.objects.all()
    davlat_dasturlari = Davlat_Dasturlari.objects.all()
    paginator = Paginator(davlat_dasturlari, 6)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'page_obj': page_obj,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'matbuot-xizmati/davlat-dasturlari.html', dic)

def davlat_dasturi(request, slug):
    admins = Administrators.objects.all()
    post = get_object_or_404(Yil_Dasturi, slug=slug)
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'post': post,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'matbuot-xizmati/davlat_dasturi.html', dic)

def announcement(request, slug):
    admins = Administrators.objects.all()
    post = get_object_or_404(Announcement, slug=slug)
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'post': post,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'announcement.html', dic)

def more_photo(request, photo_id):
    admins = Administrators.objects.all()
    photo = get_object_or_404(Photo, id=photo_id)
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'photo': photo,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'matbuot-xizmati/more_photo.html', dic)


#normativ hujjatlar

def prezident_farmonlari(request):
    admins = Administrators.objects.all()
    prezident_qarori = Prezident_Qarori.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'prezident_qarori': prezident_qarori,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'normativ-hujjatlar/prezident-qarori-va-farmonlari.html', dic)

def halq_talim(request):
    admins = Administrators.objects.all()
    halq_talim = Xalq_Talim.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'halq_talim': halq_talim,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'normativ-hujjatlar/xalq-talimi-vazirligi-hayat-qarorlari.html', dic)

def gerb(request):
    admins = Administrators.objects.all()
    gerb = Gerb.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'gerb': gerb,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'davlat-ramzlari/ozbekiston-respublikasi-davlat-gerbi.html', dic)

def gimn(request):
    admins = Administrators.objects.all()
    gimn = Gimn.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'gimn': gimn,
        'yil_dasturi': yil_dasturi,
    }
    return render(request, 'davlat-ramzlari/ozbekiston-respublikasi-davlat-madhiyasi.html', dic)

def flag(request):
    admins = Administrators.objects.all()
    flag = Flag.objects.first()
    yil_dasturi = Yil_Dasturi.objects.first()
    dic = {
        'admins': admins,
        'yil_dasturi': yil_dasturi,
        'flag': flag
    }
    return render(request, 'davlat-ramzlari/ozbekiston-respublikasi-davlat-bayrogi.html', dic)\
        
def maktab_faxri(request):
    admins = Administrators.objects.all()
    teachers = Activist.objects.all().order_by('-date')
    paginator = Paginator(teachers, 27)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.first()
    teacherr = Activist.objects.first()
    dic = {
        'admins': admins,
        'yil_dasturi': yil_dasturi,
        'page_obj': page_obj,
        'teacherr': teacherr,
    }
    return render(request, 'maktab/maktab-faxri.html', dic)

def maktab_sportchilari(request):
    admins = Administrators.objects.all()
    teachers = Sportchi.objects.all().order_by('-date')
    paginator = Paginator(teachers, 27)
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметра
    page_obj = paginator.get_page(page_number)
    yil_dasturi = Yil_Dasturi.objects.first()
    teacherr = Sportchi.objects.first()
    dic = {
        'admins': admins,
        'yil_dasturi': yil_dasturi,
        'page_obj': page_obj,
        'teacherr': teacherr,
    }
    return render(request, 'maktab/maktab-sportchilari.html', dic)
