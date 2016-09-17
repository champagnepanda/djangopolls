from django.http import HttpResponse
from django.template import loader
# Create your views here.

#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
	template = loader.get_template('polls/index.html')
	return HttpResponse(template.render(request))

