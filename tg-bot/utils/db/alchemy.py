from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    BigInteger,
    func,
    VARCHAR,
    desc,
)
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from data.config import DB_URI

engine = create_engine(DB_URI)
Base = declarative_base()


class User(Base):
    __tablename__ = "user_rano_ai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cid = Column(BigInteger, unique=True)
    whois = Column(String, default="user")
    status = Column(String, default="active")
    phonenumber = Column(String, default="null")


class Channels(Base):
    __tablename__ = "channels_rano_ai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cid = Column(String, default="None", unique=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def get_all_user():
    try:
        x = session.query(User.cid).all()
        res = [i[0] for i in x]
        return res
    finally:
        session.close()


def user_count():
    try:
        x = session.query(func.count(User.id)).first()
        return x[0]
    finally:
        session.close()


def create_user(cid):
    try:
        user = User(cid=int(cid), whois="user", status="active")
        session.add(user)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()


def get_info(cid, type_data):
    try:
        x = session.query(User).filter_by(cid=int(cid)).first()
        print(x)
        if type_data == "status":
            return x.status if x else None
        elif type_data == "whois":
            return x.whois if x else None
        elif type_data == "phonenumber":
            return x.phonenumber if x else "null"
    finally:
        session.close()

def change_info(cid, type_data, value):
    try:
        x = session.query(User).filter_by(cid=int(cid)).first()
        if type_data == "status":
            x.status = value
        elif type_data == "phonenumber":
            x.phonenumber = value
        session.commit()
        session.close()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
        return False

def get_admins():
    try:
        x = session.query(User.cid).filter_by(whois="admin").all()
        return [x[0][0]] if x else []
    finally:
        session.close()


def manage_admin(cid: int, action: str) -> bool:
    try:
        x = session.query(User).filter_by(cid=cid).first()
        if action == "add":
            x.whois = "admin"
        elif action == "rm":
            x.whois = "user"
        else:
            print("Noaniq harakat")
            return False

        session.commit()
        return True
    except SQLAlchemyError as e:
        session.rollback()
        print(e)
        return False
    finally:
        session.close()


def get_members():
    try:
        x = session.query(User).where(User.cid >= 0).all()
        return x
    finally:
        session.close()


def put_channel(channel: str):
    try:
        x = Channels(cid=channel)
        session.add(x)
        session.commit()
        return True
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
        return False


def get_channel():
    try:
        x = session.query(Channels).all()
        res = [i.cid for i in x]
        return res
    finally:
        session.close()


def get_channel_with_id():
    try:
        x = session.query(Channels).all()
        res = ""
        for channel in x:
            res += f"\nID: {channel.id} \nCID: {channel.cid}"
        return res
    finally:
        session.close()


def delete_channel(ch_id):
    try:
        x = session.query(Channels).filter_by(id=int(ch_id)).first()
        if x:
            session.delete(x)
            session.commit()
            return True
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
        return False
