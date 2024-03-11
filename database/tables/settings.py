from ..session import session
from database.model import Settings as DB_Settings

class Settings:

    @property
    @session
    def refresh_token(self, db):
        return self._get_value(db, "refresh_token")

    @refresh_token.setter
    @session
    def refresh_token(self, db, value):
        self._set(db, "refresh_token", value)

    @property
    @session
    def access_token(self, db):
        return self._get_value(db, "access_token")

    @access_token.setter
    @session
    def access_token(self, db, value):
        self._set(db, "access_token", value)

    @property
    @session
    def api_id(self, db):
        return self._get_value(db, "api_id")

    @api_id.setter
    @session
    def api_id(self, db, value):
        self._set(db, "api_id", value)

        

    def _get(self, db, key):
        return db.query(DB_Settings).filter(DB_Settings.key == key).first()

    def _get_value(self, db, key):
        obj = self._get(db, key)

        if obj:
            return obj.value

    def _set(self, db, key, value):
        obj = self._get(db, key)

        if obj:
            obj.value = value
        else:
            setting = DB_Settings(key=key, value=value)
            db.add(setting)
        db.commit()

if __name__ == "__main__":
    s = Settings()
    print(s.refresh_token)
    s.refresh_token = "test_r_t"