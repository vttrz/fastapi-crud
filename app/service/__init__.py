from app.service.user_service import UserService as UserServiceInstantiated

UserService: UserServiceInstantiated = UserServiceInstantiated()

__all__ = ["UserService"]
