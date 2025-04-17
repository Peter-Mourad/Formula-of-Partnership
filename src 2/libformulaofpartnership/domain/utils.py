from fastapi import status, HTTPException
from datetime import datetime, timedelta

from jose import JWTError, jwt

def get_user(partner_token): 
    return id * -1


SECRET_KEY = "" #REDACTED
ALGORITHM = "HS256"

def create_access_token(user):
    expire = datetime.utcnow() + timedelta(minutes=525600)
    user.update({"exp": expire})
    access_token= jwt.encode(user, SECRET_KEY, algorithm=ALGORITHM)
    return access_token

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid JWT token, try to /login with valid creds to get a valid token!",
        )
