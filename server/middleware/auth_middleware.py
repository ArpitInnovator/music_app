import os
from fastapi import Header, HTTPException  #type:ignore
import jwt   #type: ignore
from dotenv import load_dotenv   #type: ignore

load_dotenv()

key = os.getenv('key') 

def auth_middleware(x_auth_token=Header()):
    try:
        # get the user token from the header
        if not x_auth_token:
            raise HTTPException(401, 'No auth token, access denied!')

        # decode the token
        verified_token = jwt.decode(x_auth_token, key, ['HS256'])

        if not verified_token:
            raise HTTPException(401, 'Token verification failed, authorization denied')
        
        # get the id from the token
        uid = verified_token.get('id')
        return {'uid': uid, 'token': x_auth_token}
        
        # postgres database get theuser info
    except jwt.PyJWTError:
        raise HTTPException(401, 'Token is not valid, authorization failed')