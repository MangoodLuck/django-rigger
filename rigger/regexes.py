from collections import namedtuple

Regex = namedtuple('Regex', ['pattern', 'msg'])

word = Regex(r"^[a-zA-Z\u4e00-\u9fa5]+$", '只能含有字母和汉字')
