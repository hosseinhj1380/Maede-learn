__author__ = 'jrparks'
import rest_framework.relations
from django.core.urlresolvers import NoReverseMatch
from django.core.exceptions import ImproperlyConfigured


class NestedHyperlinkedRelatedField(rest_framework.relations.HyperlinkedRelatedField):
    parent_lookup_field = "parent__pk"

    def __init__(self, view_name=None, **kwargs):
        self.parent_lookup_field = kwargs.pop("parent_lookup_field", self.parent_lookup_field)
        self.parent_lookup_url_kwarg = kwargs.pop('parent_lookup_url_kwarg', self.parent_lookup_field)
        super(NestedHyperlinkedRelatedField, self).__init__(view_name=view_name, **kwargs)

    def get_object(self, view_name, view_args, view_kwargs):
        """
        Return the object corresponding to a matched URL.

        Takes the matched URL conf arguments, and should return an
        object instance, or raise an `ObjectDoesNotExist` exception.
        """
        lookup_value = view_kwargs.get(self.lookup_url_kwarg)
        parent_lookup_value = view_kwargs.get(self.parent_lookup_field)
        lookup_kwargs = {
            self.lookup_field: lookup_value,
        }
        # Try to lookup parent attr
        if parent_lookup_value:
            lookup_kwargs.update({self.parent_lookup_field: parent_lookup_value})
        return self.get_queryset().get(**lookup_kwargs)

    def get_url(self, obj, view_name, request, format):
        """
        Given an object, return the URL that hyperlinks to the object.

        May raise a `NoReverseMatch` if the `view_name` and `lookup_field`
        attributes are not configured to correctly match the URL conf.
        """
        # Unsaved objects will not yet have a valid URL.
        if obj.pk is None:
            return None

        lookup_value = getattr(obj, self.lookup_field)
        lookup_kwargs = {
            self.lookup_field: lookup_value,
        }

        # Try to lookup parent attr
        parent_lookup_value = None
        for attr in self.parent_lookup_field.split("__"):
            if not hasattr(obj, attr):
                break
            parent_lookup_value = getattr(parent_lookup_value or obj, attr)
        if parent_lookup_value:
            lookup_kwargs.update({self.parent_lookup_field: parent_lookup_value})

        return self.reverse(view_name, kwargs=lookup_kwargs, request=request, format=format)

    def to_representation(self, value):
        request = self.context.get('request', None)
        format = self.context.get('format', None)

        assert request is not None, (
            "`%s` requires the request in the serializer"
            " context. Add `context={'request': request}` when instantiating "
            "the serializer." % self.__class__.__name__
        )

        # By default use whatever format is given for the current context
        # unless the target is a different type to the source.
        #
        # Eg. Consider a HyperlinkedIdentityField pointing from a json
        # representation to an html property of that representation...
        #
        # '/snippets/1/' should link to '/snippets/1/highlight/'
        # ...but...
        # '/snippets/1/.json' should link to '/snippets/1/highlight/.html'
        if format and self.format and self.format != format:
            format = self.format

        # Return the hyperlink, or error if incorrectly configured.
        try:
            return self.get_url(value, self.view_name, request, format)
        except NoReverseMatch:
            msg = (
                'Could not resolve URL for nested hyperlinked relationship using '
                'view name "%s". You may have failed to include the related '
                'model in your API, or incorrectly configured the '
                '`lookup_field` and `parent_lookup_field` attribute on this field.'
            )
            raise ImproperlyConfigured(msg % self.view_name)


class NestedHyperlinkedIdentityField(NestedHyperlinkedRelatedField, rest_framework.relations.HyperlinkedIdentityField):
    pass