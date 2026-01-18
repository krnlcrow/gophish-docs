from importlib import import_module

class TMC:
    "Token Manipulation Collection"

    @staticmethod
    def pack(token: str, inherit: dict = {}) -> dict:
        "turn a raw string into a package of context"

        ret: dict = {
            "type" : "item", 
            "text" : token,
            "neat" : token.strip(),
            **inherit
        }
        
        if len(seg := ret["neat"].split(':', 1)) > 1:
            
            ret["type"] = "expr" 
            ret["func"] = seg[0].strip()
            ret["args"] = [*map(str.strip, seg[-1].split(','))]

        return ret

    @staticmethod
    def walk(path: str, data: dict) -> object:
        "walk a dictionary using dot-notation"

        if ('"' in path) or ("'" in path):
            return path[1:-1]
        elif path.replace('.', '', 1).isdigit():
            return path

        try:

            if len(keys := path.split('.')) == 1:
                ret = data[path]
                    
            else:        
                for key in keys:
                    data = data[key]
                ret = data

            # disallow dictionaries
            assert type(ret) not in (dict, set, list, tuple)
            return ret
        
        except (TypeError, KeyError):
            raise SyntaxError(f"invalid token: \"{path}\"")
        
        except AssertionError:
            raise SyntaxError(f"disallowed token: \"{path}\"")

    @classmethod
    def eval(cls, pack: dict, cpgn: dict) -> object:
        "interpret package as regular item"
        return cls.walk(pack["neat"], cpgn)
    
    @classmethod
    def call(cls, pack: dict, cpgn: dict) -> object:
        "interpret package as invokable"

        func, args = pack["func"], pack["args"]        
        prfx, sufx = (lst := func.split('.'))[:-1], lst[-1]

        # private functions should be safe
        if sufx.startswith('_'):
            raise PermissionError(f"forbidden method: \"{sufx}\"")
    
        try:
            module = import_module(f"mods.{'.'.join(prfx)}")
            callee = getattr(getattr(module, "Module")(), sufx)
        except ModuleNotFoundError:
            raise SyntaxError(f"invalid method: \"{func}\"")

        return callee(cpgn, *map(lambda x: TMC.walk(x, cpgn), args))