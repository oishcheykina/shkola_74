from django.urls import path
from .views import *
from django.conf.urls import handler404

handler404 = custom_page_not_found


urlpatterns = [
    path('', home, name='home'),
    path('principal/', principal, name='principal'),
    path('matbubot_hizmati/elonlar/<slug:slug>/', announcement, name='announcement'),
    path('more/<slug:slug>/', more, name='more'),
    path('school_team/', school_team, name='school_team'),
    path('lavozim_majburiyatlari/', lavozim_majburiyatlari, name='lavozim_majburiyatlari'),
    path('tarkibiy_tuzilma/', tarkibiy_tuzilma, name='tarkibiy_tuzilma'),
    path('maktab_nizomi/', maktab_nizomi, name='maktab_nizomi'),
    path('qabul_kunlari/', qabul_kunlari, name='qabul_kunlari'),
    path('maktab_madhiyasi/', maktab_madhiyasi, name='maktab_madhiyasi'),
    path('ish/', ish, name='ish'),
    path('imtihon_materiallari/', imtihon_materiallari, name='imtihon_materiallari'),
    path('qongiroqlar_jadvali/', qongiroqlar, name='qongiroqlar'),
    path('togaraklar_jadvali/', togaraklar_jadvali, name='togaraklar'),
    path('huquq-va-majburiyatlar/', huquq, name='huquq'),
    path('maktab_oquvchilarni_qabul_qilish/', oquvchilarni_qabul_qilish, name='oquvchilarni_qabul_qilish'),
    path('news/', news, name='news'),
    path('matbubot_hizmati/elonlar/', announcements, name='announcements'),
    path('photo_gallery', foto_galery, name='foto_galery'),
    path('matbubot_hizmati/photo_galery/photo/<int:photo_id>', more_photo, name='more_photo'),
    path('davlat_dasturlari/', davlat_dasturlari, name='davlat_dasturlari'),
    path('xalq_talimi/', halq_talim, name='halq_talim'),
    path('prezident_qarori/', prezident_farmonlari, name='prezident_qarori'),
    path('gerb/', gerb, name='gerb'),
    path('gimn/', gimn, name='gimn'),
    path('flag/', flag, name='flag'),
    path('maktab_faxri', maktab_faxri, name='maktab_faxri'),
    path('matbubot_hizmati/davlat_dasturlari/davalat_dasturi/year/<slug:slug>/', davlat_dasturi, name='davlat_dasturi'),
]
