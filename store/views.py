from django.shortcuts import render
from django.views import View


class HomeView(View):
    """Views for Movies List"""
    def get(self, request):
        return render(request, "base.html")
