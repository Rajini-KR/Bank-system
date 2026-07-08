from django.contrib import admin
from .models import SearchHistory


class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('city', 'search_at')
    list_filter = ('search_at',)
    search_fields = ('city',)


admin.site.register(SearchHistory, SearchHistoryAdmin)