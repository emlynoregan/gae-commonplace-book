from datetime import datetime
from google.appengine.datastore.datastore_query import Cursor

def ProcessStandardParams(aQueryMessage, aClass):
    if hasattr(aQueryMessage, "on_or_before") and aQueryMessage.on_or_before:
        ldtOnOrBefore = datetime.utcfromtimestamp(aQueryMessage.on_or_before)
        lquery = aClass.query(aClass.dtStored <= ldtOnOrBefore)
    else:
        lquery = aClass.query()
    return lquery

def Fetch(aQueryMessage, aQuery):
    if hasattr(aQueryMessage, "limit") and hasattr(aQueryMessage, "cursor"):          
        if hasattr(aQueryMessage, "cursor") and aQueryMessage.cursor:
            lresults, lcursor, lmore = aQuery.fetch_page(aQueryMessage.limit, start_cursor = Cursor(urlsafe=aQueryMessage.cursor))
        else:
            lresults, lcursor, lmore = aQuery.fetch_page(aQueryMessage.limit)
    else:
        lresults, lcursor, lmore = aQuery.fetch_page(10)
        
    return lresults, lcursor, lmore
    