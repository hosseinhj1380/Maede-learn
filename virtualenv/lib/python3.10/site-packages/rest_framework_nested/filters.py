__author__ = 'jrparks'
import rest_framework.filters


class NestedFilterBackend(rest_framework.filters.BaseFilterBackend):
    # TODO: Change to mixins and remove this hack
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(**view.kwargs)