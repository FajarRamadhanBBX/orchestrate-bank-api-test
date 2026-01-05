from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Account(Base):
    __tablename__ = "accounts"

    id_user = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True, nullable=False)
    balance = Column(Numeric, default=0.0)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    from_account = Column(String, nullable=False)
    to_account = Column(String, nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)