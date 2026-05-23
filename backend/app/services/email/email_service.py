
from fastapi import BackgroundTasks, APIRouter
from backend.app.core.settings import settings
import secrets
import resend

resend.api_key = settings.resend_api_key
#
# r = resend.Emails.send(
#     {
#         "from": "onboarding@resend.dev",
#         "to": "daniel.j.sterzel@gmail.com",
#         "subject": "Hello World",
#         "html": "<p> I just did it my guy... </p>",
#     }
# )

token = secrets.token_urlsafe(32)