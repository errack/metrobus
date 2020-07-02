from flask import Flask, request
from flask_restful import Resource, Api
from config_loader.configuration_loader import ConfigurationLoader
from data_loader.data_loader import DataLoader

load_config = ConfigurationLoader.load_config("config/config.yml")
app = Flask(__name__)
api = Api(app)

sources = DataLoader(load_config)

class MetrobusById(Resource):

    def get(self,vehicle_id):
        data = request.form.to_dict(flat=False)
        return sources.find_by_unit_metrobus(vehicle_id)

class MetrobusByAlcaldia(Resource):
    def get(self,alcaldia):
        data = request.form.to_dict(flat=False)
        return sources.find_by_alcaldia(alcaldia)

api.add_resource(MetrobusById, '/findMetrobus/vehicleId/<vehicle_id>')
api.add_resource(MetrobusByAlcaldia, '/findMetrobusByAlcaldia/alcaldia/<alcaldia>')


if __name__=='__main__':
    app.run(debug=True)