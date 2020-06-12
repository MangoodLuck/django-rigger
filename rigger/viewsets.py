from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rigger.mixin import UpdateMixin, DestroyMixin


class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   UpdateMixin,
                   DestroyMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass

