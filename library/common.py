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
    # DESCRIPTION : Get current timestamp
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
    
common = Common()