from django import template
from django.utils.timezone import localtime

register = template.Library()

@register.filter(name='format_date')
def format_date(value):
    """
    自定义模板过滤器，格式化日期为'YYYY年MM月DD日 HH:MM'格式
    
    用法：{{ comment.created|format_date }}
    """
    # 转换为本地时间
    local_dt = localtime(value)
    # 格式化为'YYYY年MM月DD日 HH:MM'
    return local_dt.strftime('%Y年%m月%d日 %H:%M')