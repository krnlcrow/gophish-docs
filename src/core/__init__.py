from zoneinfo import ZoneInfo
from os       import sep

env = {
    
    "api" : {
        "host" : "127.0.0.1",
        "port" : 3333,
        "auth" : "407b85550c255eda2e283e1889532e3695d75541deb844257e8ac22af92e7d99",
        "zone" : ZoneInfo("Europe/Amsterdam"),
    },

    "/" : sep,
    "." : sep.join(__file__.split(sep)[:-3])

}