#!/usr/bin/python3

from email.utils import parsedate_to_datetime
from zoneinfo import ZoneInfo
from lilaclib import *


def pre_build():
    schema_version = _G.newvers[0]

    dt = parsedate_to_datetime(_G.newvers[1])
    dict_version = dt.astimezone(ZoneInfo("Asia/Shanghai")).strftime("%Y%m%d")

    for line in edit_file('PKGBUILD'):
        if line.startswith('_schema_version='):
            line = f'_schema_version={schema_version}'
        if line.startswith('_dict_version='):
            line = f'_dict_version={dict_version}'
        print(line)

    pkgver = f'{schema_version}+r{dict_version}'
    update_pkgver_and_pkgrel(pkgver)
