from django.views import generic


class HomepageView(generic.TemplateView):
    template_name = 'article/homepage.html'
