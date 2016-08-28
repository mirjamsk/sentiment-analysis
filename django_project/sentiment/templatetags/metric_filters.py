from django import template

register = template.Library()


@register.filter(name='prettify_api_id')
def prettify_api_id(api_id):
    return api_id\
        .replace('_', ' ')\
        .replace('api', 'API ')\
        .replace('sentiment', '')\
        .replace('neutral', 'neutral label')


@register.filter(name='collection_itemize')
def collection_itemize(metric={}):
    html = ''
    for sentiment in metric.keys():
        html += '<div class ="collection-item"> {0}: {1}</div>'.format(sentiment, metric[sentiment])
    return html
