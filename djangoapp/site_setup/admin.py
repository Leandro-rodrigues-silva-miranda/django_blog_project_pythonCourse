from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from site_setup.models import MenuLink, SiteSetup

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id','text','url_or_path',
    list_display_links = 'id','text','url_or_path',
    search_fields = 'id','text','url_or_path',

class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1



@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title','description',
    exclude = 'links',
    inlines = MenuLinkInline,
    
    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
    
    def changeform_view(self, request: HttpRequest, object_id: str | None = ..., form_url: str = ..., extra_context: dict[str, bool] | None = ...) -> Any:
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        return super().changeform_view(request, object_id, form_url, extra_context)