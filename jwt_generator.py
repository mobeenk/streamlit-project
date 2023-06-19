import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'callreports123456789callreports123456789'
# http://localhost:8501/?token=

def generate_jwt_token(user_id, username):
    # should generate token contains loggedin user data (id, username etc ...)
    # Set the expiry date
    expiry_date = datetime.utcnow() + timedelta(days=10)  # Token expires in 1 day

    # Create the payload
    payload = {
        'id': user_id,
        'exp': expiry_date,
        'username': username,

    }
    # Generate the JWT token
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return jwt_token


def is_valid_jwt(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'], options={"verify_signature": False})
        return True
    except jwt.ExpiredSignatureError:
        print("JWT token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid JWT token.")

    return False


def get_user_claims(token):
    isValid = is_valid_jwt(token)
    print('is valid jwt: ' + token)
    print(isValid)
    if isValid:
        print('TOKENN STATUS')
        print(read_jwt_token(token))
        user_id = read_jwt_token(token)[0]
        return user_id, read_jwt_token(token)[1], read_jwt_token(token)[2]
    else:
        return None, None, None


def read_jwt_token(jwt_token):
    try:
        # Decode the JWT token
        decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])

        # Extract the payload data
        user_id = decoded_token.get('id')
        expiry_date = decoded_token.get('exp')
        username = decoded_token.get('username')

        # Return the extracted data
        return user_id, expiry_date, username

    except jwt.ExpiredSignatureError:
        # Handle token expiration error
        print("Token has expired.")
        return None, None, None

    except jwt.InvalidTokenError:
        # Handle invalid token error
        print("Invalid token.")
        return None, None, None


new_token = generate_jwt_token(5, "Moubien")
print(new_token)
# print(read_jwt_token(new_token))
# datetime_obj = datetime.fromtimestamp(read_jwt_token(new_token)[1])
# print(datetime_obj)
