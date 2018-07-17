from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator
from video.models import Video


class VideoTranslationOptions(TranslationOptions):
    fields = ('head', 'body', 'link',)


translator.register(Video, VideoTranslationOptions)
