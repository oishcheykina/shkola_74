import re
from django import template

register = template.Library()

def replace_youtube_links(content):
    youtube_regex = r"https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)"
    
    def replacement(match):
        video_id = match.group(1)
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        iframe_code = f'<!--dle_media_begin:{youtube_url}--><iframe width="100%" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe><!--dle_media_end-->'
        return iframe_code

    return re.sub(youtube_regex, replacement, content)

@register.filter(name='youtube_embed')
def youtube_embed(content):
    """Фильтр для замены ссылок на YouTube на iframe-код"""
    return replace_youtube_links(content)
