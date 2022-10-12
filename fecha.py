
import sys
from datetime import datetime


def format_date(mydate):
        print("The original string is : " + str(mydate))
        format = "%Y-%m-%d"
        res = True
        try:
            res = bool(datetime.strptime(mydate, format))
        except ValueError:
            res = False
            objDate = datetime.strptime(mydate, "%d/%m/%Y")
            datetime.strftime(objDate,"%Y-%m-%d")
            print("The new string is : " + str(objDate)[:10])
            return str(objDate)[:10]
        print("Does date match format? : " + str(res))
        return(mydate)
        
if __name__ == "__main__":
    
    gpus = sys.argv[1]
    format_date(gpus)