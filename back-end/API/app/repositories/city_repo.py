from flask import jsonify
from app import db, app
from app.models.city_model import City
from app.models.region_model import Region

class CityRepo:

        def getCity(self, data):
            city = City.query.filter_by(city=data['city']).first()
            region = Region.query.filter_by(id=city.idRegion).first()
            if not city:
                return jsonify({'message': 'no city found'})
            return jsonify({'city': city.city, 'region': region.region})
    
        def getAllCities(self):
            cities = City.query.all()
            output = []
            if not cities:
                return jsonify({'message': 'no cities found'})
            for city in cities:
                city_data = {}
                city_data['id'] = city.id
                city_data['city'] = city.city
                city_data['region'] = Region.query.filter_by(id=city.idRegion).first().region
                output.append(city_data)
            return jsonify({'cities': output})
        
