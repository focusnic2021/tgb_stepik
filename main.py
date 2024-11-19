import math
import pprint
from typing import Tuple

print('Hello world!')


def foo(x: int) -> Tuple[int, float]:
    return x, math.pi


pprint.pprint('Курс Разработка телеграм-бота на библиотеке aiogram')

print(foo(4))
