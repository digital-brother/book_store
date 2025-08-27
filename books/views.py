from django.http import JsonResponse
from django.views import View


class BookListView(View):
    def get(self, request):
        return JsonResponse({'books': []})
