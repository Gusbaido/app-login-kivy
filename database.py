import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    email, password, name, created = line.strip().split(";")
                    self.users[email] = (password, name, created)
        except FileNotFoundError:
            with open(self.filename, "w") as file:
                pass  # Cria o arquivo se não existir

    def get_user(self, email):
        return self.users.get(email, -1)

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (
                password.strip(),
                name.strip(),
                DataBase.get_date()
            )
            self.save()
            return 1
        else:
            print("Email já existente.")
            return -1

    def validate(self, email, password):
        user = self.get_user(email)
        if user != -1:
            return user[0] == password
        return False

    def save(self):
        with open(self.filename, "w") as file:
            for user in self.users:
                file.write(
                    user + ";" +
                    self.users[user][0] + ";" +
                    self.users[user][1] + ";" +
                    self.users[user][2] + "\n"
                )

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
