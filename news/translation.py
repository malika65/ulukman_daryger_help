from modeltranslation.translator import register, TranslationOptions
from .models import News, People,Newspaper,ForumInfo


@register(News)
class NewsTranslationOptions(TranslationOptions):

    fields = ('title','body')


@register(People)
class PeopleTranslationOptions(TranslationOptions):
    fields = ('name','story')



@register(Newspaper)
class NewspaperTranslationOptions(TranslationOptions):

    fields = ('title_paper','date_created')



@register(ForumInfo)
class ForumInfoTranslationOptions(TranslationOptions):

    fields = ('title','subtitle','info')