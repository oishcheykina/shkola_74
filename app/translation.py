from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')  # Поля, которые нужно переводить
    
@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('name', 'field')
    
@register(Lavozim_Majburiyatlari)
class Lavozim_MajburiyatlariTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'image')
    
@register(Tarkibiy_Tuzilma)
class Tarkibiy_TuzilmaTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'image')
    
@register(Maktab_Nizomi)
class Maktab_NizomiTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'image')
    
@register(Maktab_Madhiyasi)
class Maktab_MadhiyasiTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'image')
    
@register(Qubul_Kunlari)
class Qubul_KunlariTranslationOptions(TranslationOptions):
    fields = ('day', 'time', 'lunch')
    
@register(Ish)
class IshTranslationOptions(TranslationOptions):
    fields = ('content', 'conclusion')

    
@register(Imtihon_Materiallari)
class Imtihon_MateriallariTranslationOptions(TranslationOptions):
    fields = ('content',)
    
@register(Administrators)
class AdministratorsTranslationOptions(TranslationOptions):
    fields = ('name', 'field')
    
@register(Principal)
class PrincipalTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'date_of_birth', 'education', 'field', 'reception_days')
    
@register(Tugaraklar)
class TugaraklarTranslationOptions(TranslationOptions):
    fields = ('title', 'grade', 'days', 'teacher',)