from django import template


register = template.Library()


@register.filter(name='youtube_image')
def youtube_image(value):
    link = value.split("?v=")[1]
    youtube_link = "https://img.youtube.com/vi/" + link + "/mqdefault.jpg"
    return youtube_link


@register.filter(name='youtube_code')
def youtube_code(value):
    link = value.split("?v=")[1]
    youtube_link = "https://www.youtube.com/embed/" + link + '?html5=1'
    return youtube_link
