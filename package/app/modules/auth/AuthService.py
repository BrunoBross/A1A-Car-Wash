from package.app.modules.auth.AuthView import AuthView


class AuthService:

    @staticmethod
    def start():
        val = AuthView.login()
        print(val)
