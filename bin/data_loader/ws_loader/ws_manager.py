from .web_services import WebService
from .ws_exceptions import ExceptionBadConfigurationWebService


HOST="host"
URL="url"
PARAMSREQUIRED="req_params"
PARAMSOPTIONAL="opt_params"
PORT="port"

class WSManager():

    def __init__(self, ws_config:dict):
        self.ws_list = []

        self.ws_list = self._load_web_services_configurated(
                        self._map_ws_configurated(ws_config))

    def _map_ws_configurated(self,ws_configured:dict):
        _ws_list = []
        _ws_created = []

        for ws in ws_configured[constant.WEB_SERVICES].keys():
            if ws.get(constant.HOST,None) is None or ws.get(constant.URL,None) is None:
                _msg = "Required attributes [{},{}]"
                _except = ExceptionBadConfigurationWebService(_msg)
            if ws not in _ws_created:
                _ws_list.append(ws,ws_configured[ws], _except)

        return _ws_list

    def _load_web_services_configurated(self, ws_configured:list):
        _list_wservices = []
        [_list_wservices.append(WebService(ws[1],ws[2],ws[3]))
         for ws in ws_configured]
        return _list_wservices 
    
    def _find_ws(self, ws_id:str)->WebService:
        _ws_finded = None
        _finded = filter(lambda x: x.equals(ws_id), self.ws_list)
        if len(_finded)>0:
            _ws_finded = _finded[-1]
        return _ws_finded
    



