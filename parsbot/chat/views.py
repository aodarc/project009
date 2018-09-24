from django.views.generic import TemplateView


class ChatBotTemplateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Parse Bot'
        return context
