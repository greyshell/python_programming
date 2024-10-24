from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, Date
from sqlalchemy.orm import relationship


base = declarative_base()


class DBCustomer(base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fast_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)


class DBRoom(base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(250), nullable=False)
    size = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


class DBBooking(base):
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True, autoincrement=True)

    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    customer = relationship(DBCustomer)

    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    room = relationship(DBRoom)

    price = Column(Integer, nullable=False)
