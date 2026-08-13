from email.message import EmailMessage
import aiosmtplib
from .config import settings


async def send_verification_email(
    recipient_email: str,
    verification_token: str
):
    verification_link = (
        f"http://127.0.0.1:8000/user/verify-email"
        f"?token={verification_token}"
    )
    message = EmailMessage()
    message["From"] = (
        f"{settings.mail_from_name} "
        f"<{settings.mail_from_email}>"
    )
    message["To"] = recipient_email
    message["Subject"] = "Verify your email"
    message.set_content(
        f"""
Hello,
Thank you for registering.
Please verify your email by clicking this link:
{verification_link}
If you did not create this account, ignore this email.
Thanks
"""
    )

    await aiosmtplib.send(
        message,
        hostname=settings.mailtrap_host,
        port=settings.mailtrap_port,
        username=settings.mailtrap_username,
        password=settings.mailtrap_password,
        start_tls=True
    )