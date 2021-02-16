from django.views import generic
from blog.forms import ParserForm
from blog.parse import parser


class ParseView(generic.TemplateView):
    template_name = 'parser.html'
    form_class = ParserForm


class ShowParseView(generic.TemplateView):
    template_name = 'show.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        image, price = parser(self.request.GET.get('url'))
        ctx['image'] = image
        ctx['price'] = price
        return ctx
