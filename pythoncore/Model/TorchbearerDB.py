from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..Vault import get_key

__connection_string = get_key('torchbearerdb-connection-string')

Engine = create_engine(__connection_string, echo=False, pool_recycle=3600)

# Create session maker, to be used throughout application
Session = sessionmaker(bind=Engine)
