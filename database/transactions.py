from sqlalchemy import select, insert, update, delete, Table
from sqlalchemy.exc import SQLAlchemyError
from .db_config import get_db

def getAll(table: Table)->list:
    #manejo de error
    try:
        #obtener sesion de bd
        db = get_db()
        #obtener el statement
        stmt = select(table)
        result = db.execute(stmt)
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]
    except SQLAlchemyError as e:
        return []
    finally:
        db.close()
        
def get(table: Table, col: str, value: any)->dict | None:
    #manejo de error
    try:
        #obtener sesion de bd
        db = get_db()
        #obtener el statement
        stmt = select(table).where(table.c[col] == value)
        result = db.execute(stmt)
        row = result.fetchone()
        return dict(row._mapping) if row else None
    except SQLAlchemyError as e:
        return None
    finally:
        db.close()

def getLike(table: Table, like: str)->list:
    #manejo de error
    try:
        #obtener sesion de bd
        db = get_db()
        #obtener el statement
        stmt = select(table).where(table.c.name.like(f"%{like}%"))
        result = db.execute(stmt)
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]
    except SQLAlchemyError as e:
        return []
    finally:
        db.close()
        
def create(table: Table, data: dict)->bool:
    #manejo de error
    try:
        #obtener sesion de bd
        db = get_db()
        #obtener el statement
        stmt = insert(table).values(data)
        db.execute(stmt)
        db.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        return False
    finally:
        db.close()
        
def modify(table: Table, data: dict)->bool:
    #manejo de error
    try:
        #obtener sesion de bd
        db = get_db()
        #obtener el statement
        stmt = update(table).where(table.c.id == data['id']).values(data)
        db.execute(stmt)
        db.commit()
        return True
    except SQLAlchemyError as e:
        return False
    finally:
        db.close()
        
def drop(table: Table, id: str | int)->bool:
    #manejo de error
    try:
        #obtener sesion de bd
        db = get_db()
        #obtener el statement
        stmt = delete(table).where(table.c.id == id)
        db.execute(stmt)
        db.commit()
        return True
    except SQLAlchemyError as e:
        return False
    finally:
        db.close()