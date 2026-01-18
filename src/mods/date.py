from datetime import datetime

class Module:

    @staticmethod
    def format(_, date: str, frmt: str) -> str:    
        "format dates and times"

        return datetime.fromisoformat(date)\
            .strftime(frmt.strip())