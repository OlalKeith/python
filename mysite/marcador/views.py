from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from .models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.public.all()
    context = {'bookmarks': bookmarks}
    return render(request, 'marcador/bookmark_list.html', context)