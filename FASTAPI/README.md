# FastAPI Authentication Notes

## Overview
This project now supports JWT-based access token verification and fetching the currently authenticated user.

## What was added
- Access token creation in [app/oauth2.py](app/oauth2.py)
- Access token verification using JWT decoding
- A dependency function to get the current logged-in user from the database

## Authentication flow
1. A user logs in via the login endpoint.
2. The server returns a Bearer access token.
3. The token is sent in the `Authorization` header for protected routes.
4. The server verifies the token and loads the matching user from the database.

## Main functions
- `create_access_token(data, expires_delta=None)`
  - Creates a JWT access token.
- `verify_access_token(token, credentials_exception)`
  - Validates the token and extracts the `user_id` from the payload.
- `get_current_user(token, db)`
  - Returns the authenticated user based on the verified token.

## Example request
Use the token like this:

```http
Authorization: Bearer <access_token>
```

## How to test
- Open the login endpoint and generate a token.
- Use the token in the Authorization header for a protected route.
- If the token is invalid or expired, the API returns a `401 Unauthorized` response.

## Environment-driven configuration
- The settings schema in [app/config.py](app/config.py) now defines required fields only, so sensitive and connection values are read from the environment file instead of being hard-coded in the class body.
- The runtime picks the database host, port, username, password, database name, JWT secret, algorithm, and access-token lifetime from the values loaded from [app/.env](app/.env).
- The JWT creation flow in [app/oauth2.py](app/oauth2.py) uses the configured expiry window from the settings object, rather than a direct `15`-minute fallback inside the function.

## Notes
- The secret key and algorithm are defined in [app/oauth2.py](app/oauth2.py).
- The authentication logic uses `OAuth2PasswordBearer` and SQLAlchemy.
