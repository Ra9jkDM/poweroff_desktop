from __future__ import annotations
from typing import Final, List

from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, Session

from pysqlcipher3 import dbapi2 as sqlite

db_name = "power.db"
password = "pwd9889" # Change me!!!
ENGINE = create_engine(f"sqlite+pysqlcipher://:{password}@/{db_name}?kdf_iter=256000&cipher_plaintext_header_size=32")


def get_engine():
    return ENGINE


Base = declarative_base()

class Settings(Base):
    __tablename__  = "settings"

    key: Mapped[String] = mapped_column(String, primary_key=True, nullable=False)
    value: Mapped[String] = mapped_column(String, nullable=False)

    def __str__(self):
        return f"Settings(key={self.key}, value={self.value})"

def create_db():
    Base.metadata.create_all(bind=ENGINE)

def create_data():
    with Session(autoflush=True, bind=ENGINE) as db:
        s1 = Settings(key="refresh_token", value="SHA1_0823498_grid")
        s2 = Settings(key="access_token", value="MD4_u9902")

        db.add(s1)
        db.add(s2)
        db.commit()

def select_all():
    with Session(autoflush=True, bind=ENGINE) as db:
        data = db.query(Settings).all()
        
        for i in data:
            print(i)

if __name__ == "__main__":
    create_db()
    # create_data()
    select_all()

# python -m database.model