from django.shortcuts import render
from django.views import View


class BookListView(View):
    def get(self, request):
        return render(request, "books/book_list.html", {"books": []})
