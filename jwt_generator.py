import jwt
from datetime import datetime, timedelta


def generate_jwt_token(user_id):
    # should generate token contains loggedin user data (id, username etc ...)
    # Set the expiry date
    expiry_date = datetime.utcnow() + timedelta(days=10)  # Token expires in 1 day

    # Create the payload
    payload = {
        'id': user_id,
        'exp': expiry_date,
        'username': 'Moubien',

    }
    # Generate the JWT token
    jwt_token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')

    return jwt_token


def read_jwt_token(jwt_token):
    try:
        # Decode the JWT token
        decoded_token = jwt.decode(jwt_token, 'your_secret_key', algorithms=['HS256'])

        # Extract the payload data
        user_id = decoded_token.get('id')
        expiry_date = decoded_token.get('exp')
        username = decoded_token.get('username')

        # Return the extracted data
        return user_id, expiry_date, username

    except jwt.ExpiredSignatureError:
        # Handle token expiration error
        print("Token has expired.")
        return None, None

    except jwt.InvalidTokenError:
        # Handle invalid token error
        print("Invalid token.")
        return None, None


def is_valid_jwt(token, secret_key):
    try:
        jwt.decode(token, secret_key, algorithms=['HS256'], options={"verify_signature": False})
        return True
    except jwt.ExpiredSignatureError:
        print("JWT token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid JWT token.")

    return False

new_token = generate_jwt_token(5)
print(new_token)
# print(read_jwt_token(new_token))
# datetime_obj = datetime.fromtimestamp(read_jwt_token(new_token)[1])
# print(datetime_obj)
