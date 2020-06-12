from rest_framework import status
from abc import ABCMeta, abstractmethod
from rigger.response import APIResponse
from rigger.settings import api_settings


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
