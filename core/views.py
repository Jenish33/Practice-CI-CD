from django.http import HttpResponse

def home(request):
   text = """<h1>This is now belongs to jenish</h1>"""
   return HttpResponse(text)