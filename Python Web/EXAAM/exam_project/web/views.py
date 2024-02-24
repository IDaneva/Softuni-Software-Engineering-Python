from django.shortcuts import render

from django.views import generic as views


# class IndexView(views.TemplateView):
#     template_name = 'html_templates/base.html'

def index(request):
    return render(request, 'html_templates/base.html')
