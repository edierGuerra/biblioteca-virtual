from database.db import SessionLocal,Base,engine
from database.models import book,user
#Fabrica de sesiones
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Función para crear todas las tablas
def create_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("¡Tablas creadas exitosamente!")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")