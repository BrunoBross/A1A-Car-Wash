from package.app.api.crypt.utils import encrypt
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.api.model.User import User
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.meta.Singleton import Singleton


class UserDtoMapper(metaclass=Singleton):
    def mapUserToDto(self, user: User) -> UserDto:
        return UserDto(id=user.id, username=user.username, role=RoleEnum(user.role.id))

    def mapDtoToUser(self, userDto: UserDto) -> User:
        return User(
            username=userDto.username,
            password=encrypt(userDto.password),
            role_id=userDto.role.value,
        )
