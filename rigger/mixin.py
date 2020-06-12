from rest_framework import status
from abc import ABCMeta, abstractmethod
from rigger.response import APIResponse
from rigger.settings import api_settings
from rest_framework.mixins import UpdateModelMixin

class DestroyModelClass(metaclass=ABCMeta):
    """
     meta class :  Destroy a model instance.
     info :  model  __str__
     judge: True or False
    """

    @abstractmethod
    def destroy(self, request, *args, **kwargs):
        instance = kwargs.get("instance")
        info = kwargs.get("info")
        judge = kwargs.get("judge")

        if judge:
            return APIResponse(data_status=api_settings.DATA_STATUS["failed"],
                               data_msg="{} exists，please clean it ".format(info),
                               status=status.HTTP_406_NOT_ACCEPTABLE)

        self.perform_destroy(instance)

        return APIResponse(data_status=api_settings.DATA_STATUS["success"],
                           data={"name": str(instance)},  # model  __str__
                           status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.logical_delete()


class DestroyMixin(DestroyModelClass):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        judge = self.judge_destroy()

        res = super().destroy(self, request, instance=self.get_object(),
                              info=str(self.get_object()), judge=judge)
        return res

    def judge_destroy(self):
        """
        if your don't wanna to destory , please return True
        :return: True or False
        """
        pass


class UpdateMixin(UpdateModelMixin):
    """
    Update a model instance response like:
    {
        "flag": 20000,
        "msg": "success",
        "data": {
            "name": {
                "old": "device3",
                "new": "device-3"
            }
        }
    }
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)  # default patch
        instance = self.get_object()

        update_fields = {}
        for field in request.data.items():
            _field, _ = field
            update_fields[_field] = {"old": getattr(instance, _field)}

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        for field in request.data.items():
            _field, _value = field
            update_fields[_field]["new"] = _value

        return APIResponse(data_status=api_settings.DATA_STATUS["success"],
                           data=update_fields,
                           status=status.HTTP_201_CREATED)
