from django.shortcuts import render

def main_page(request):
    return render(request, 'view_news/index.html')
