import uuid
from datetime import date, datetime
from datetime import timedelta as td

class Common:

    #---------------------------
    # FUNCTION: generate uuid #
    #---------------------------
    def uuid_generator(self):
        return str(uuid.uuid4())
    

    # ------------------------------------
    # FUNCTION: get_timestamp
    # ------------------------------------
    def get_timestamp(self, wtime=0):

        if wtime:
            timestamp = str(
                (datetime.utcnow() + td(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
            )
        else:
            timestamp = str(
                (datetime.utcnow() + td(hours=8)).strftime("%Y-%m-%d")
            )

        return timestamp
    
    #----------------------------------------------
    # SET OLD ID AND REVISION FOR UPDATING DOCUMENT
    #----------------------------------------------
    def clean_couch_doc(self, doc):
        if "_id" in doc:
            doc["id"] = doc["_id"]
            del doc["_id"]
        if "_rev" in doc:
            doc["rev"] = doc["_rev"]
            del doc["_rev"]

        return doc

    
common = Common()