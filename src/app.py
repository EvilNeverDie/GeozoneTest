import databases
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/geozones/")
def create_geozone(geozone: schemas.GeozoneCreate, db: Session = Depends(get_db)):
    db_geo = models.Geozone(**geozone.dict())
    db.add(db_geo)
    db.commit()
    return geozone.dict()