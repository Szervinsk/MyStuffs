from app.models.user_account import UserAccount
import json
import uuid

class DataRecord:

    def __init__(self):
        self._user_accounts = []  # Mudança para um underscore
        self._authenticated_users = {}  # Mudança para um underscore
        self.read()

    def read(self):
        try:
            with open("app/controllers/db/user_accounts.json", "r") as arquivo_json:
                user_data = json.load(arquivo_json)
                self._user_accounts = [UserAccount(**data) for data in user_data]
        except FileNotFoundError:
            self._user_accounts.append(UserAccount('Guest', '010101', '101010'))

    def book(self, username, password):
        new_user = UserAccount(username, password)
        self._user_accounts.append(new_user)
        with open("app/controllers/db/user_accounts.json", "w") as arquivo_json:
            user_data = [self.user_to_dict(user_account) for user_account in self._user_accounts]
            json.dump(user_data, arquivo_json)

    def user_to_dict(self, user_account):
        return {
            'username': user_account.username,
            'password': user_account.password
        }

    def getCurrentUser(self, session_id):
        return self._authenticated_users.get(session_id, None)

    def getUserName(self, session_id):
        user = self.getCurrentUser(session_id)
        return user.username if user else None

    def checkUser(self, username, password):
        print(f'checkUser => username: {username}, senha: {password}')
        for user in self._user_accounts:
            if user.username == username and user.password == password:
                session_id = str(uuid.uuid4())
                self._authenticated_users[session_id] = user
                return session_id
        return None

    def compareUsers(self, username):
        for user in self._user_accounts:
            if user.username == username:
                return True  # Já existe um usuário
        return False  # Não existe um usuário

    def logout(self, session_id):
        if session_id in self._authenticated_users:
            del self._authenticated_users[session_id]
