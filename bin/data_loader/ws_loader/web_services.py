import urllib.request as req
from urllib.error import HTTPError
import json

from .ws_exceptions import ExceptionBadConfigurationWebService

HOST="host"
URL="url"
PARAMSREQUIRED="req_params"
PARAMSOPTIONAL="opt_params"
PORT="port"

class WebService():


    def __init__(self, ws_id:str, ws_conf:dict, ws_notations:Exception):
        self.ws_id = ws_id
        self.notation = ws_notations
        self.__build_ws(ws_conf)

    def __build_ws(self, ws_conf:dict):
        if self.notation is not ExceptionBadConfigurationWebService:
            self.request_query = "{}{}{}".format(
                ws_conf.get(HOST),
                ws_conf.get(URL),
                ws_conf.get(PARAMSREQUIRED,"")
            ).strip()
            self.opt_params = ws_conf.get(PARAMSOPTIONAL,"")

    def request(self, opt_params:list=[]):
        _request_query = self.__process_opt_params(opt_params)
        try:
            _response = req.urlopen(_request_query,timeout=30)
            _records = json.loads(_response.read()).get("records")
            


            _result = {"status":200,"content":_records}
        except HTTPError as e:
            return self.__error(e)
        return _result

    def __process_opt_params(self, params:list):
        _request_wiht_param = "{}".format(self.request_query)
        if len(params)>0:
            for param in params:
                _to_replace = "<{}>".format(param[0])
                _request_wiht_param = _request_wiht_param.replace(_to_replace,param[1])
                print(_request_wiht_param)
        return _request_wiht_param

    def __error(self, error:Exception):
        return {"status":error.code, "content":error.msg}

    def equals(self, ws_id:str):
        return True if self.ws_id == ws_id else False
 