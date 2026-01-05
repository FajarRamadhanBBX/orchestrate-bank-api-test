from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Account(Base):
    __tablename__ = "accounts"

    id_user = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True, nullable=False)
    balance = Column(Numeric, default=0.0)