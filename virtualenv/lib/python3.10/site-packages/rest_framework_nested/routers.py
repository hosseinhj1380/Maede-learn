__author__ = 'jrparks'
import rest_framework.routers


class SimpleRouter(rest_framework.routers.SimpleRouter):
    """
    SimpleRouter for nested routers.
    """
    def __init__(self, trailing_slash=True):
        self.nested_routers = []
        super(SimpleRouter, self).__init__(trailing_slash)

    def _register_nested_router(self, router):
        """
        NestedSimpleRouter.__init__ calls this method
        """
        assert issubclass(router.__class__, NestedSimpleRouter), "You can only register NestedSimpleRouters"
        self.nested_routers.append(router)

    def get_urls(self):
        """
        Returns a list of urls including all NestedSimpleRouter urls
        """
        ret = super(SimpleRouter, self).get_urls()
        for router in self.nested_routers:
            ret.extend(router.get_urls())
        return ret


class DefaultRouter(SimpleRouter, rest_framework.routers.DefaultRouter):
    """
    DefaultRouter for nested routers.
    """
    pass


class NestedSimpleRouter(SimpleRouter):
    """
    A nested implementation of the SimpleRouter
    """

    def __init__(self, parent_router, parent_prefix, *args, **kwargs):
        """
        Initialize a nested router
        """
        self.parent_router = parent_router
        self.parent_prefix = parent_prefix
        self.nest_count = getattr(parent_router, 'nest_count', 0) + 1
        self.nest_prefix = kwargs.pop('lookup', 'nested_%i' % self.nest_count) + '__'
        super(NestedSimpleRouter, self).__init__(*args, **kwargs)

        parent_registry = [registered for registered in self.parent_router.registry if registered[0] == self.parent_prefix]
        try:
            parent_prefix, parent_viewset, parent_basename = parent_registry[0]
        except:
            raise RuntimeError("Parent registry not found.")

        nested_routes = []
        parent_lookup_regex = parent_router.get_lookup_regex(parent_viewset, self.nest_prefix)
        self.parent_regex = r'{parent_prefix}/{parent_lookup_regex}/'.format(
            parent_prefix=parent_prefix,
            parent_lookup_regex=parent_lookup_regex,
        )
        if hasattr(parent_router, "parent_regex"):
            self.parent_regex = parent_router.parent_regex + self.parent_regex

        for route in self.routes:
            route_contents = route._asdict()
            route_contents['url'] = route.url.replace('^', '^' + self.parent_regex)
            nested_routes.append(type(route)(**route_contents))
        self.routes = nested_routes
        self.parent_router._register_nested_router(self)