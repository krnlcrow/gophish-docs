from core.api import API
from core.tmc import TMC

from argparse  import ArgumentParser
from importlib import import_module

class CLI:

    def __init__(self):
        
        parser = ArgumentParser()

        for arg in ("id", "format", "template", "output"):
            
            parser.add_argument(
                f"-{arg[0]}", f"--{arg}",
                action   = "store",
                required = True
            )

        self.args = parser.parse_args().__dict__

    def __main__(self) -> None:
         
        sets = list()
        cpgn = dict({
            **API.request(f"campaigns/{self.args['id']}"),"stats":\
              API.request(f"campaigns/{self.args['id']}/summary")["stats"]
        })

        try:
            modl = import_module(f"core.out.{self.args["format"].lower()}")
        except ModuleNotFoundError:
            raise Exception(f"invalid format: \"{self.args["format"]}\"")
        
        for token in (mod := modl.Format(self.args["template"])).get():
                
            pack  = TMC.pack(token)
            sets += [{**pack,
                "eval": {
                    "item": TMC.eval,
                    "expr": TMC.call
                }[pack["type"]](pack, cpgn)}]
            
        mod.set(self.args["output"], sets)
        

if __name__ == "__main__":
    (_ := CLI()).__main__()