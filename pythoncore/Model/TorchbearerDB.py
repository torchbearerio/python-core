from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..Vault import get_key
from Hit import Hit


__connection_string = get_key('torchbearerdb-connection-string')

__engine = create_engine(__connection_string, echo=False)

# Create session maker, to be used throughout application
Session = sessionmaker(bind=__engine)

