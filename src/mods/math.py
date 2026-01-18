class Module:
    
    @staticmethod
    def add(_, a: int, b: int) -> int: return int(a) + int(b)
    @staticmethod
    def sub(_, a: int, b: int) -> int: return int(a) - int(b)
    @staticmethod
    def dif(_, a: int, b: int) -> int: return abs(int(a) - int(b))
    
    @staticmethod
    def pct(_, a: int, b: int) -> str:
        "retrieve ratio"

        return f"{int(a) / int(b) * 100:.2f}" \
            if all([a, b]) else '0'