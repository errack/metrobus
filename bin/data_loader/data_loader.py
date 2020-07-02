import matplotlib.path as mplPath
import numpy as np

from .source_factory import DataSourceFactory


class DataLoader:
    def __init__(self, config:dict):
        self.sources=self.config_data_loader(config)
    
    def config_data_loader(self, config:dict):
        return  DataSourceFactory.build(config)

    def find_by_unit_metrobus(self, id_unit:str):
        _result = {}
        _data = self.get_data_metrobus()
        if _data.get("status") != 200:
            return _data
        else:
            _result["status"]=200
            _records = [x.get("fields") for x in _data.get("content")
                        if x.get("fields").get("vehicle_id") == id_unit]
            if len(_records) == 1:

                _result["message"]="success"
                _content = {'vehicle_id':id_unit,
                            'date_updated':_records[0].get("date_updated"),
                            'position_longitude':_records[0].get("position_longitude"),
                            'position_latitude': _records[0].get("position_latitude"),
                            }
                _result["content"]=_content
            else:
                _result["message"]="Vehicle : {} not found".format(id_unit)
        
        return _result

    def find_by_alcaldia(self,alcaldia:str):
        _result = {}
        _vehicles = self.get_data_metrobus()
        _alcaldia = self.get_data_alcaldias(alcaldia)

        if _vehicles.get("status") != 200: 
            return _vehicles
        elif _alcaldia.get("status") != 200:
            return _alcaldia
        else:
            _result["status"]=200
            _coordinates = _alcaldia.get("content")[-1].get("fields").get("geo_shape").get("coordinates")[0]
            _shape_alcaldia = mplPath.Path(np.array(_coordinates))
            _fund_vehicle_in_alcaldia = []
            for vehicle in _vehicles.get("content"):
                _point_vehicle = vehicle.get("geometry").get("coordinates")
                _id = vehicle.get("fiels")
                if _shape_alcaldia.contains_point((_point_vehicle[0],_point_vehicle[1])):
                    _fund_vehicle_in_alcaldia.append(vehicle)
            
            if len(_fund_vehicle_in_alcaldia)>0:
                _result["content"] = _fund_vehicle_in_alcaldia
                _result["message"]="success"
            else:
                _alcaldia_name = _alcaldia.get("content")[-1].get("fields").get("nomgeo")
                _result["message"]="Vehicles not found in {}".format(_alcaldia_name)
        return _result


    def get_data_metrobus(self):
        data_metrobus = self.__find_source("metrobus").request([])
        return data_metrobus
    
    def get_data_alcaldias(self,alcaldia):
        _data_alcaldias = self.__find_source("geo_alcaldias").request([("ALCALDIA",alcaldia)])
        return _data_alcaldias


    def __find_source(self, source):
        _source = list(filter(lambda x: x.equals(source), self.sources))

        if len(_source):
            return _source[-1]
        else: 
            return None