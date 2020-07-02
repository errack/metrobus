from .ws_loader.web_services import WebService

class DataSourceFactory:

    @staticmethod
    def build(conf):
        sources = []
        _srcs = conf.get("sources")
        for source in _srcs.keys():
            _type = _srcs.get(source).get("type")
            if _type == "web-service":
                _conf = _srcs.get(source).get("config")
                print(_conf)
                _id = _conf.get("id")
                sources.append(WebService(_id, _conf,None))
        return sources
