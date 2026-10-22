
from email.message import EmailMessage

import aiosmtplib
from .config import settings


async def send_verification_email(
    recipient_email: str,
    verification_token: str,
):
    verification_link = (
        "http://127.0.0.1:8000/user/verify-email"
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
        f"""Hello,

Thank you for registering.

Verify your email using this link:
{verification_link}

If you did not create this account, ignore this email.
"""
    )

    await aiosmtplib.send(
        message,
        hostname=settings.mailtrap_host,
        port=settings.mailtrap_port,
        username=settings.mailtrap_username,
        password=settings.mailtrap_password,
        start_tls=True,
    )


async def send_password_reset_email(
    recipient_email: str,
    reset_token: str,
):
    message = EmailMessage()
    message["From"] = (
        f"{settings.mail_from_name} "
        f"<{settings.mail_from_email}>"
    )
    message["To"] = recipient_email
    message["Subject"] = "Reset your password"

    message.set_content(
        f"""Hello,

We received a request to reset your password.

Your password reset token is:

{reset_token}

This token expires in 15 minutes and can only be used once.

Open your application and submit this token with your new
password to the POST /user/reset-password endpoint.

If you did not request this, ignore this email.
"""
    )

    await aiosmtplib.send(
        message,
        hostname=settings.mailtrap_host,
        port=settings.mailtrap_port,
        username=settings.mailtrap_username,
        password=settings.mailtrap_password,
        start_tls=True,
    )
