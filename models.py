class User:
    def __init__(self, username = "", password = "", salt = ""):
        self._id = -1
        self.username = username
       # self._hashed_password = hash_password(password, salt)
        self._hashed_password = password
    @property
    def id(self):
        return self._id
    @property
    def hashed_password(self):
        return self._hashed_password

    def set_password(self, password, salt=""):
        # self._hashed_password = hash_password(password, salt)
        self._hashed_password = password

    @hashed_password.setter
    def hashed_password(self, password):
        self.set_password(password)
    def save_to_db(self, cursor):
        if self.id == -1:
            sql = """
                INSERT INTO users(username, hashed_password)
                VALUES(%s, %s) RETURNING id
            """
            values = (self.username, self.hashed_password)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]
            return True
        return False


