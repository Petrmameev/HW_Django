import datetime

from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book
from datetime import datetime

def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)

# def books_pub_view(request, pub_date='2015-03-11'):
#     # book = request.GET.get(pub_date=pub_date)
#     pub_date = datetime.strptime(pub_date, '%Y-%m-%d')
#     # format = '%Y-%m-%d'
#     # CONTENT = Book.objects.all()
#     template = 'books/book_date.html/'
#     # paginator = Paginator(CONTENT, 1)
#     # current_page = int(request.GET.get(pub_date, '2015-03-11'))
#     # # book = request.GET.get('pub_date')
#     # context = {'book': paginator.get_page(current_page),
#     #            'page': paginator.get_page(current_page)
#     #            }
#     context = {'books': Book}
#     return render(request, template, context)

# def book_view(request, slug):
#     template = 'books/book.html'
#     context = {'book': Book.objects.get(slug=slug)}
#     return render(request, template, context)