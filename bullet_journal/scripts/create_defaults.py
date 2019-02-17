from ..models.collection import Collection
from ..constants import collection_types
from ..db import db

def create_default_collections():
    try:
        db.session.add(
            Collection(name='Index', type=collection_types.INDEX)
        )
        db.session.add(
            Collection(name='Future Log', type=collection_types.FUTURE)
        )
        db.session.add(
            Collection(name='Monthly Log', type=collection_types.MONTHLY)
        )
        db.session.add(
            Collection(name='Daily Log', type=collection_types.DAILY)
        )
        db.session.commit()
    except:
        print("Unable to add default collections to DB")
        db.session.rollback()
