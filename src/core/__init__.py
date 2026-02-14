from zoneinfo import ZoneInfo
from os       import sep

env = {
    
    "api" : {
        "host" : "127.0.0.1",
        "port" : 3333,
        "auth" : "dd2a70611fb9ad818d2cbb593486d27229fbfea65f2ae343a23f9e20d6bf80b7",
        "zone" : ZoneInfo("Europe/Amsterdam"),
    },

    "/" : sep,
    "." : sep.join(__file__.split(sep)[:-3])

}