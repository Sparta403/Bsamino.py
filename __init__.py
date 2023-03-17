from json import loads
from requests import get

__title__ = 'BSAmino'
__author__ = 'SFAH'
__license__ = 'Kratos'
__copyright__ = 'Copyright 2021-2022 AKATSKI'
__version__ = '1.1'

from .BSamino import *
from .utils import *


__newest__ = loads(get("https://t.me/spi22der").text)["info"]["version"]

if __version__ != __newest__:
    print(f"New version of {__title__} available: {__newest__} (Using {__version__})")
else:
    print(f"version : {__version__}")
