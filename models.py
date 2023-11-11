from clcrypto import hash_password
class User:
    def __init__(self, username = "", password = "", salt = ""):
        self._id = -1
        self.username = username
        self._hashed_password = hash_password(password, salt)
    @property
    def id(self):
        return self._id
    @property
    def hashed_password(self):
        return self._hashed_password

    def set_password(self, password, salt=""):
        self._hashed_password = hash_password(password, salt)

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
        else:
            sql = """
                UPDATE Users SET username=%s, hashed_password=%s
                WHERE id=%s
            """
            values = (self.username, self.hashed_password, self.id)
            cursor.execute(sql, values)
            return True


    @staticmethod
    def load_user_by_id(cursor, id_):
        sql = "SELECT id, username, hashed_password FROM users WHERE id=%s"
        cursor.execute(sql, (id_,))
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None


    @staticmethod
    def load_user_by_username(cursor, username):
        sql = "SELECT id, username, hashed_password FROM users WHERE username=%s"
        cursor.execute(sql, (username,))
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User()
            loaded_user._id = id_
            loaded_user.username = username
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        sql = "SELECT id, username, hashed_password FROM Users"
        users = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            id_, username, hashed_password = row
            loaded_user = User()
            loaded_user._id = id_
            loaded_user.username = username
            loaded_user._hashed_password = hashed_password
            users.append(username)
        return users
    def delete(self, cursor):
        sql = "DELETE FROM Users WHERE username=%s"
        cursor.execute(sql, (self.username,))
        self._id = -1
        return True


class Messages:
    def __init__(self, from_id="", to_id="", creation_date=None, text=""):
        self._id = -1
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self.creation_date = creation_date

    @property
    def id(self):
        return self._id

    def save_to_db(self, cursor):
        if self.id == -1:
            sql = """
            INSERT INTO messages(from_id, to_id, creation_date, text) 
            VALUES(%s, %s, %s, %s) RETURNING id
            """
            values = (self.from_id, self.to_id, self.creation_date, self.text)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]
            return True
        return False
    @staticmethod
    def load_messages(cursor):
        sql = "select text from messages;"
        cursor.execute(sql)
        messages = []
        for row in cursor.fetchall():
            text = row
            messages.append(text)
        return messages

