class Module:

    @staticmethod
    def upper(_, text: str) -> str: return text.capitalize()
    @staticmethod
    def lower(_, text: str) -> str: return text.lower()
    
    @staticmethod
    def ifnull(_, obj: object, alt: str) -> object:
        "return val if it's not null, else alt"
        return obj if obj else alt
    
    @staticmethod
    def plural(_, value: int, single: object, multi: object) -> object:
        "support plurality e.g. 'user' vs 'users'"

        if value == 1:
            return single
        
        return multi