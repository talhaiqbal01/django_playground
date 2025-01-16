from django.shortcuts import render

posts = [
    {
        'author': 'Talha Iqbal',
        'title': 'Blog post 1',
        'content': 'First post\'s content here...',
        'created_at': '15th of January, 2025.',
    },
    {
        'author': 'Hamza Munir',
        'title': 'Blog post 2',
        'content': 'Second post\'s content here...',
        'created_at': '11th of January, 2025.',
    },
    {
        'author': 'Umair Asad',
        'title': 'Blog post 3',
        'content': 'Third post\'s content here...',
        'created_at': '16th of January, 2025.',
    },
]


def home(request):
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context= {'title': 'About'}
    return render(request, 'blog/about.html', context)
