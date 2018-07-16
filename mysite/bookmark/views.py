from django.views.generic import ListView
from bookmark.models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark
