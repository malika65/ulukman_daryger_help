from django.contrib import admin
from .models import People
from django import forms
from django.utils.safestring import mark_safe
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

from .models import News, People, NewsImage,Newspaper,Comments,PaymentsInfo,ForumInfo,Gallery,ShowPhoto,Appeal,Enterpreneurship,EnterpreneImage
from .forms import ShowAdminForm
from django.template.loader import get_template
from django.utils.translation import gettext as _

from .models import Gallery, ShowPhoto
from .forms import ShowAdminForm


class ShowPhotoInline(admin.TabularInline):
    model = ShowPhoto
    fields = ("showphoto_thumbnail",)
    readonly_fields = ("showphoto_thumbnail",)
    max_num = 0

    def showphoto_thumbnail(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("show_thumbnail.html")
        return tpl.render({"photo": instance.photo})

    showphoto_thumbnail.short_description = _("Thumbnail")



@admin.register(Gallery)
class ShowAdmin(admin.ModelAdmin):
    form = ShowAdminForm
    inlines = [ShowPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)

        
admin.site.register(Comments)
admin.site.register(PaymentsInfo)
admin.site.register(Appeal)

@admin.register(ForumInfo)
class ForumInfoAdmin(TranslationAdmin):
    list_display = ("title", "subtitle","info","img_info","date_created")
    list_display_links = ("title",)



@admin.register(Newspaper)
class NewspaperAdmin(TranslationAdmin):
    """Газета"""
    list_display = ("title_paper", "pdf","date_created")


class NewsImageAdmin(admin.StackedInline):
    model = NewsImage


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    """Новости"""
    list_display = ("title", "body","date_created")
    inlines = [NewsImageAdmin]
    list_display_links = ("title",)



@admin.register(People)
class PeopleAdmin(TranslationAdmin):
    list_display = ("name", "story","pic","date_created_women","PEOPLE_CHOICES")
   

class EnterpreneImageAdmin(admin.StackedInline):
    model = EnterpreneImage


@admin.register(Enterpreneurship)
class EnterpreneurshipAdmin(TranslationAdmin):

    list_display = ("name", "text")
    inlines = [EnterpreneImageAdmin]
    list_display_links = ("name",)



admin.site.site_title = "Улукман Дарыгер"
admin.site.site_header = "Улукман Дарыгер"
