__author__ = 'jrparks'
from django.utils.translation import ugettext_lazy as _
from django.db import models as db_models
import rest_framework.serializers

import relations


class NestedHyperlinkedModelSerializer(rest_framework.serializers.HyperlinkedModelSerializer):
    default_error_messages = {
        'invalid': _('Invalid data. Expected a dictionary, but got {datatype}.'),
        'no_parent': _('Model has no ForeignKey field. Specify the field `parent_model` in your Meta.'),
        'multiple_parents': _('Model has too many ForeignKey fields. Specify the field `parent_model` in your Meta.'),
    }
    serializer_related_field = relations.NestedHyperlinkedRelatedField
    serializer_url_field = relations.NestedHyperlinkedIdentityField

    def build_nested_field(self, field_name, relation_info, nested_depth):
        """
        Create nested fields for forward and reverse relationships.
        """

        class NestedSerializer(NestedHyperlinkedModelSerializer):
            class Meta:
                model = relation_info.related_model
                depth = nested_depth - 1

        field_class = NestedSerializer
        field_kwargs = rest_framework.serializers.get_nested_relation_kwargs(relation_info)

        return field_class, field_kwargs

    def build_url_field(self, field_name, model_class):
        """
        Create a field representing the object's own URL.
        """
        field_class = self.serializer_url_field
        field_kwargs = rest_framework.serializers.get_url_kwargs(model_class)
        field_kwargs.update({"parent_lookup_field": self.get_parent_lookup_field()})
        return field_class, field_kwargs

    def get_parent_lookup_field(self):
        """
        Return tha parent_lookup_field for the NestedHyperlinkedModelSerializer.
        If `parent_lookup_field` of `parent_model` is not defined lookup ForeignKey field of model.
        :return: parent_lookup_field
        """
        if hasattr(self.Meta, "parent_lookup_field"):
            return getattr(self.Meta, "parent_lookup_field")
        elif hasattr(self.Meta, "parent_model"):
            model = getattr(self.Meta, "parent_model")
        else:
            parent_models = filter(
                lambda field: isinstance(field, db_models.ForeignKey),
                self.Meta.model._meta.fields
            )
            assert len(parent_models) > 0, self.default_error_messages['no_parent']
            assert len(parent_models) == 1, self.default_error_messages['multiple_parents']
            model = parent_models[0].related_model

        return '%(model_name)s__pk' % {
            'app_label': model._meta.app_label,
            'model_name': model._meta.object_name.lower()
        }