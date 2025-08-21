#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("25292226", cast=int)
    API_HASH = config("a7d366626f54ca13916a01bd4ef121ab")
    BOT_TOKEN = config("7878942070:AAHWQ4VjCd9DtTI3Q4W-zLLlde4i1_SzqYE")
    OWNER = config("OWNER_ID", default=7445035418, cast=int)
    LOG = config("-1002480003193", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
