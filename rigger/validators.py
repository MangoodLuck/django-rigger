from rest_framework import serializers
import re


def PhoneValidator(value):
    phone = value.split(";")
    for p in phone:
        if not re.match(r'1[35678]\d{9}', p):
            raise serializers.ValidationError("手机格式不正确: {}".format(p))
    return ";".join(phone)


def IpaddrValidator(value):
    if not re.match(r"^[0-9\.;-]+$", value):
        raise serializers.ValidationError("只能含有 /数字/./;/-")
    return value


def IpaddrPoolValidator(value):
    if not re.match(r"^[0-9\.;-]+$", value):
        raise serializers.ValidationError("只能含有 /数字/./;/-")
    return value


def EmailValidator(value):
    if not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', value):
        raise serializers.ValidationError("邮箱格式不正确: {}".format(value))
    return value


def NumValidator(value):
    if not re.match(r"^[0-9]+$", value):
        raise serializers.ValidationError("只能含有数字")
    return value


def WordNumCenterlineValidator(value):
    if not re.match(r"^[\u4e00-\u9fa5a-zA-Z0-9-]+$", value):
        raise serializers.ValidationError("只能含有 字母/汉字/数字/中线")
    return value


class RegexValidator(object):
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        reg = self.base
        if not re.match(reg.pattern, value):
            message = '{}'.format(reg.msg)
            raise serializers.ValidationError(message)
