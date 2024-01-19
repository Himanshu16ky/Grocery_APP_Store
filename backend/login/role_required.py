from functools import wraps
from db.database import Users
from flask_jwt_extended import get_jwt_identity

def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            identity = get_jwt_identity()
            user = Users.query.filter_by(username=identity).first()

            if user and (isinstance(allowed_roles, list) and user.role in allowed_roles) or (isinstance(allowed_roles, str) and user.role == allowed_roles):
                return func(*args, **kwargs)
            else:
                return False
        return wrapper
    return decorator