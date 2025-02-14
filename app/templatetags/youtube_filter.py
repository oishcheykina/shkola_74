import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

YOUTUBE_REGEX = r'(https?://www\.youtube\.com/watch\?v=|https?://youtu\.be/)([\w-]+)'

@register.filter(name='youtube_iframe')
def youtube_iframe(value):
    """Заменяет ссылку YouTube на адаптивный iframe без обрезки видео"""
    match = re.search(YOUTUBE_REGEX, value)
    if match:
        video_id = match.group(2)
        iframe_code = (
            f'<div class="video-container">'
            f'<iframe src="https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1&showinfo=0&controls=1&fs=1&playsinline=1" '
            f'frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" '
            f'allowfullscreen></iframe>'
            f'</div>'
        )
        return mark_safe(iframe_code)
    return value