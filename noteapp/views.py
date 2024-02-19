from django.shortcuts import render
from .models import Quote
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, get_object_or_404
from .models import Quote, User 

def main(request):
    return render(request, 'noteapp/index.html')

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'noteapp/quote_list.html', {'quotes': quotes})

def scrape_quotes(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            authors = soup.find_all('span', class_='author')
            quotes = soup.find_all('span', class_='text')
            for author, quote in zip(authors, quotes):
                author_name = author.get_text()
                quote_text = quote.get_text()
                author_obj, created = User.objects.get_or_create(name=author_name)
                Quote.objects.create(author=author_obj, text=quote_text)
            return render(request, 'scraping_success.html')
    return render(request, 'scrape_quotes.html')

def author_detail(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    quotes = author.quote_set.all()
    return render(request, 'noteapp/author_detail.html', {'author': author, 'quotes': quotes})