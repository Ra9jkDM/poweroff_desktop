from __future__ import annotations
from typing import Final, List

from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, Session

from pysqlcipher3 import dbapi2 as sqlite

# engine = create_engine("sqlite:///power.db")
db_name = "power_enc.db"
password = "pwd9889"
# engine = create_engine(f"sqlite+pysqlcipher://:{password}@/{db_name}?cipher=aes-256-cfb&kdf_iter=64000")
engine = create_engine("sqlite+pysqlcipher://:testing@/foo.db?kdf_iter=256000&cipher_plaintext_header_size=32")
# cipher=aes-256-cfb&
Base = declarative_base()

class LoginInformation(Base):
    __tablename__  = "login_info"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    refresh_token: Mapped[String] = mapped_column(String, unique=True, nullable=False)
    access_token: Mapped[String] = mapped_column(String, unique=True, nullable=False)

    def __str__(self):
        return f"LoginInfo({self.id}, {self.refresh_token}, {self.access_token})"

def create_db():
    Base.metadata.create_all(bind=engine)

    # with Session(autoflush=True, bind=engine) as db:
    #     info = LoginInformation(refresh_token="test_token_r", access_token="new_ascces_token")
    #     db.add(info)
    #     db.commit()

def select_all():
    with Session(autoflush=True, bind=engine) as db:
        data = db.query(LoginInformation).all()
        
        for i in data:
            print(i)
if __name__ == "__main__":
    create_db()
    select_all()