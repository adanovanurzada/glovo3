from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CountryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Store)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('store_name', 'description', 'address')

@register(Contact)
class ActorTranslationOptions(TranslationOptions):
    fields = ('title' ,)

@register(Product)
class GenreTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')

@register(Combo)
class MovieTranslationOptions(TranslationOptions):
    fields = ('combo_name', 'description')

