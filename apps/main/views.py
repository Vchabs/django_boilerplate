from django.views.generic import TemplateView
#Quick home page
class Home(TemplateView):
    template_name = "home.html"