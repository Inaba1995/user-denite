class User:
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'
        self._users = []


    def get_user_id(self) -> int:
        return self._user_id

    def get_name(self) -> str:
        return self._name

    def get_access_level(self) -> str:
        return self._access_level

    # Сеттеры
    def set_name(self, name: str):
        self._name = name

    @classmethod
    def add_to_system(cls, user):
        cls._users.append(user)

    @classmethod
    def remove_from_system(cls, user_id):
        cls._users = [user for user in cls._users if user.get_user_id() != user_id]

    @classmethod
    def get_all_users(cls):
        return cls._users


class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, user_id: int, name: str):
        if self.get_access_level() == 'admin':
            new_user = User(user_id, name)
            User.add_to_system(new_user)
            print(f"Пользователь {name} добавлен в систему")
        else:
            print("У вас нет прав на добавление пользователей")

    def remove_user(self, user_id: int):
        if self.get_access_level() == 'admin':
            User.remove_from_system(user_id)
            print(f"Пользователь с ID {user_id} удален из системы")
        else:
            print("У вас нет прав на удаление пользователей")

    def list_users(self):
        if self.get_access_level() == 'admin':
            users = User.get_all_users()
            for user in users:
                print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
        else:
            print("У вас нет прав на просмотр списка пользователей")
