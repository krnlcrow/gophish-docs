from base64 import b64encode

class Format:
    "Markdown Document"

    def __init__(self, path: str) -> None:

        self.into = '{'
        self.exit = '}'
        self.path = path

        with open(path, 'r', encoding="utf-8", errors="replace") as file:
            self.text = file.read()

    def get(self) -> list[str]:
        
        token, dumps, istkn, array =\
              str(), str(), bool(), list()
        
        for char in self.text:

            if char == self.into or istkn:
                token += char             
                istkn = True

            if char == self.exit:
                array += [token[1:-1]]
                istkn, token = False, ''
        
            # error checking
            dumps += char

        if (dumps.count(self.into) + dumps.count(self.exit)) % 2 != 0:
            raise SyntaxError(f"odd token-syntax: \"{self.path}\"")

        return array

    def set(self, path: str, packs: list[dict]) -> None:
        
        for pack in packs:
            
            # reapply terminators
            pack["text"] = self.into + \
                pack['text'] + self.exit

            if type(pack["eval"]) == bytes:     
                
                pack["eval"] = (
                    r"![](data:image/png;base64,"
                    f"{b64encode(pack["eval"]).decode()})"
                )

            # insert evaluated
            self.text = self.text.replace(
                pack["text"], str(pack["eval"])
            )
        
        with open(path, 'w', encoding="utf-8", errors="replace") as file:
            file.write(self.text)