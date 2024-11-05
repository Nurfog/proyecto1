from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def courses(request):
    return render(request, 'pages/courses.html')

def team(request):
    return render(request, 'pages/team.html')

def contact(request):
    return render(request, 'pages/contact.html')

def blog(request):
    return render(request, 'pages/blog.html')

def testimonial(request):
    return render(request, 'pages/testimonial.html')

def error_404(request):
    return render(request, '404.html', status=404)