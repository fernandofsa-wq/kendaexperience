from django.contrib import admin

from .models import (Contato, DataEvento, Eventos, Galeria, InscricaoDetalhe,
                     InscricaoItem, Patrocinio, RegulamentoDetalhe,
                     RegulamentoItem, Sliders, Sobre)

admin.site.site_header = 'Kenda (Administração)'
admin.site.site_title = 'Kenda'


class SlidersAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'is_published']
    list_display_links = 'titulo',
    search_fields = 'titulo',
    list_filter = 'is_published',
    list_per_page = 10
    list_editable = 'is_published',


admin.site.register(Sliders, SlidersAdmin)


class PatrocinioAdmin(admin.ModelAdmin):
    list_display = ['id', 'patrocinador', 'is_published']
    list_display_links = 'patrocinador',
    search_fields = 'patrocinador',
    list_filter = 'is_published',
    list_per_page = 10
    list_editable = 'is_published',


admin.site.register(Patrocinio, PatrocinioAdmin)


class RegulamentoItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'is_published']
    list_display_links = 'titulo',
    search_fields = 'titulo',
    list_filter = 'is_published',
    list_per_page = 10
    list_editable = 'is_published',


admin.site.register(RegulamentoItem, RegulamentoItemAdmin)


class EventosAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'datainicio', 'datafim', 'is_published']
    list_display_links = 'titulo',
    search_fields = 'titulo', 'datainicio', 'datafim',
    list_filter = 'is_published',
    list_per_page = 10
    list_editable = 'is_published',


admin.site.register(Eventos, EventosAdmin)


class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'evento', 'img', 'is_published']
    list_display_links = 'titulo',
    search_fields = 'titulo', 'evento',
    list_filter = 'is_published',
    list_per_page = 10
    list_editable = 'is_published',


admin.site.register(Galeria, GaleriaAdmin)


class DataEventoAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['id', 'titulo', 'data']
    list_display_links = 'titulo',
    list_editable = 'data',

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(DataEvento, DataEventoAdmin)


class SobreAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['id', 'titulo']
    list_display_links = 'titulo',

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Sobre, SobreAdmin)


class InscricaoItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'link', 'is_published']
    list_display_links = 'titulo',
    search_fields = 'titulo',
    list_filter = 'is_published',
    list_per_page = 10
    list_editable = 'is_published',


admin.site.register(InscricaoItem, InscricaoItemAdmin)


class InscricaoDetalheAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['id', 'titulo']
    list_display_links = 'titulo',

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(InscricaoDetalhe, InscricaoDetalheAdmin)


class RegulamentoDetalheAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['id', 'titulo']
    list_display_links = 'titulo',

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(RegulamentoDetalhe, RegulamentoDetalheAdmin)


class ContatoAdmin(admin.ModelAdmin):

    list_display = ['data', 'nome', 'phone',
                    'email', 'assunto', 'message', 'lido']
    list_display_links = 'data',
    search_fields = 'nome', 'assunto', 'message',
    list_filter = 'lido',
    list_per_page = 10
    list_editable = 'lido',

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Contato, ContatoAdmin)
