from datetime import datetime, timedelta, UTC
from typing import Any

import jwt

"""
Access token - 15 minutes

- user id
- exp
- token type

Refresh token - 30 days


| claim | meaning    |
| ----- | ---------- |
| sub   | user id    |
| exp   | expiration |
| iat   | issued at  |
| typ   | token type |

"""

class JWTUtils:
    @staticmethod
    def create_access_token():
        pass

    @staticmethod
    def create_refresh_token():
        pass

    @staticmethod
    def decode_token():
        pass