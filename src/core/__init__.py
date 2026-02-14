from zoneinfo import ZoneInfo
from os       import sep

env = {
    
    "api" : {
        "host" : "127.0.0.1",
        "port" : 3333,
        "auth" : "<API_KEY>",
        "zone" : ZoneInfo("Europe/Amsterdam"),
    },

    "/" : sep,
    "." : sep.join(__file__.split(sep)[:-3])

}
