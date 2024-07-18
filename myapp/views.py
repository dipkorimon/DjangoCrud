from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models_sqlalchemy import Book, session

def book_list(request):
  books = session.query(Book).all()
  return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
  book = session.query(Book).get(pk)
  return render(request, 'books/book_detail.html', {'book': book})

def book_create(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    author = request.POST.get('author')
    published_date = request.POST.get('published_date')
    isbn = request.POST.get('isbn')

    new_book = Book(title=title, author=author, published_date=published_date, isbn=isbn)
    session.add(new_book)
    session.commit()
    
    return redirect('book_list')
  return render(request, 'books/book_form.html')

def book_update(request, pk):
  book = session.query(Book).get(pk)
  if request.method == 'POST':
    book.title = request.POST.get('title')
    book.author = request.POST.get('author')
    book.published_date = request.POST.get('published_date')
    book.isbn = request.POST.get('isbn')
    
    session.commit()
    
    return redirect('book_list')
  return render(request, 'books/book_form.html', {'book': book})

def book_delete(request, pk):
  book = session.query(Book).get(pk)
  session.delete(book)
  session.commit()
  return redirect('book_list')
