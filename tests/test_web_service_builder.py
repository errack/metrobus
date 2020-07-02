import sys
import unittest
import os

sys.path.insert(0,'bin')

from config_loader.configuration_loader import ConfigurationLoader
from data_loader.data_loader import DataLoader
from data_loader.ws_loader.web_services import WebService

class TestWebServiceBuilder(unittest.TestCase):
    def setUp(self):
        self.path_configuration = "./tests/input_files/config.yml"
        self._config_vehicle = {"type":'web-service',
                                    "config":{
                                        "id": 'metrobus',
                                        "host": 'https://datos.cdmx.gob.mx',
                                        "url": '/test/url'
                                    }
                                }
        self.assert_conf = {"sources":{
                                "movilidad":self._config_vehicle,
                                "alcaldia":{"type":'web-service',
                                    "config":{
                                        "id": 'geo_alcaldias',
                                        "host": 'https://datos.cdmx.gob.mx',
                                        "url": '/api/records/1.0/search/?dataset=limite-de-las-alcaldias&q=&rows=16&facet=nomgeo&refine.cve_mun=<ALCALDIA>'
                                    }
                                }
                            }
        }

    def test_configuraation_loader(self):
        _config = ConfigurationLoader.load_config(self.path_configuration)
        self.assertEquals(_config,self.assert_conf)
    
    def test_web_service_loader(self):
        _id_vehicle = "01010101"

        sources = DataLoader(self.assert_conf)
        _ws = WebService("geo_alcaldias",self._config_vehicle.get("config"),None)
        _result_ws = _ws.request()
        
        _result_resources = sources.find_by_unit_metrobus(_id_vehicle)
        self.assertEquals(_result_ws,_result_resources)