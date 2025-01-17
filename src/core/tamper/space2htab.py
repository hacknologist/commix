#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of Commix Project (https://commixproject.com).
Copyright (c) 2014-2025 Anastasios Stasinopoulos (@ancst).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

For more see the file 'readme/COPYING' for copying permission.
"""

from src.utils import settings
from src.thirdparty.six.moves import urllib as _urllib

"""
About: Replaces space character ('%20') with horizontal tab ('%09')
Notes: This tamper script works against all targets.
"""

__tamper__ = "space2htab"
space2htab = "%09"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  settings.TAMPER_SCRIPTS[__tamper__] = True
  if len(settings.WHITESPACES) != 0:
    if settings.WHITESPACES[0] == _urllib.parse.quote(settings.SINGLE_WHITESPACE):
      settings.WHITESPACES[0] = space2htab
    elif space2htab not in settings.WHITESPACES:
      settings.WHITESPACES.append(space2htab)
  return payload

# eof