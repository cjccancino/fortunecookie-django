# Six
import six

# Django
from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, format_html_join
from django.utils.translation import ugettext_lazy as _
try:
    from django.urls import reverse
except ImportError:  # pragma: no cover
    from django.core.urlresolvers import reverse

# Django-FortuneCookie
from fortunecookie.models import FortuneCookie


class OccurrencesListFilter(admin.SimpleListFilter):
    """Filter lists by number of occurrences in fortune cookies."""

    title = _('fortune cookie occurrences')
    parameter_name = 'fortune_cookies__count'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        occurrences = set(filter(None, qs.values_list(self.parameter_name, flat=True)))
        return [(x, six.text_type(x)) for x in sorted(occurrences)]

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(fortune_cookies__count=self.value())


class OccurrencesMixin(object):
    """Mixin to annotate queries with count of fortune cookies."""

    def get_queryset(self, request):
        qs = super(OccurrencesMixin, self).get_queryset(request)
        return qs.annotate(Count('fortune_cookies'))

    def get_occurrences_display(self, obj=None):
        url = reverse('admin:fortunecookie_fortunecookie_changelist')
        return format_html('<a href="{}?{}={}">{}</a>', url,
                           self.occurrences_lookup, obj.pk, obj.occurrences)

    get_occurrences_display.short_description = _('Occurrences')
    get_occurrences_display.allow_tags = True
    get_occurrences_display.admin_order_field = 'fortune_cookies__count'


class FortuneCookieAdmin(admin.ModelAdmin):
    """Admin configuration for fortune cookies."""

    list_display = ('fortune', 'created', 'modified')
    fields = ('fortune', 'created', 'modified')
    readonly_fields = ('created', 'modified')

    def get_queryset(self, request):
        qs = super(FortuneCookieAdmin, self).get_queryset(request)


admin.site.register(FortuneCookie, FortuneCookieAdmin)
