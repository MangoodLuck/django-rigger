from rest_framework.response import Response
from rest_framework import status


class APIResponse(Response):
    """
    export a standard response info
    like
    {
        "flag": "",
        "msg": "",
        "data": ""
    }
    """

    def __init__(self, data_status=None, data_msg=None, data=None,
                 status=status.HTTP_200_OK, content_type=None,
                 headers=None, exception=False, **kwargs):

        if data_status is None:
            raise ValueError("data_status is required")

        format_data = {
            "flag": data_status,
            "msg": "",
            "data": ""
        }
        if str(data_status).startswith("2"):
            format_data["msg"] = "success"

        if data_msg is not None:
            format_data["msg"] = data_msg

        if data is not None:
            format_data["data"] = data

        if kwargs is not None:
            for k, v in kwargs.items():
                if k != "hook_param":
                    setattr(format_data, k, v)
                else:
                    self.__hook(k)
        super().__init__(data=format_data, status=status, headers=headers,
                         exception=exception, content_type=content_type)

    def __hook(self, hook_param):
        pass
