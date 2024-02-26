from flask import jsonify, request
from app import db, app
from app.models.city_model import City
from app.models.region_model import Region
from app.controllers.user_controller import token_required

@app.route('/getCity', methods=['GET'])
@token_required
def getCity(self):
    city_id = request.args.get('id')
    if not city_id:
        return jsonify({'message': 'City parameter is missing'}), 400
    city = City.query.filter_by(id=city_id).first()
    if not city:
        return jsonify({'message': 'No city found'}), 404
    region = Region.query.filter_by(id=city.idRegion).first()
    return jsonify({'id': city.id, 'city': city.city, 'region': region.region})

@app.route('/getAllCities', methods=['GET'])
@token_required
def getAllCities(self):
    cities = City.query.all()
    output = []
    if not cities:
        return jsonify({'message': 'no cities found'})
    for city in cities:
        city_data = {}
        city_data['id'] = city.id
        city_data['city'] = city.city
        city_data['idRegion'] = city.idRegion
        output.append(city_data)
    return jsonify({'cities': output})