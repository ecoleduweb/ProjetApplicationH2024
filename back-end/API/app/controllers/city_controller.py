from flask import jsonify, request
from app import db, app
from app.models.city_model import City
from app.models.region_model import Region
from app.controllers.user_controller import token_required

@app.route('/city', methods=['GET'])
@token_required
def city(self):
    city_id = request.args.get('id')
    if not city_id:
        return jsonify({'message': 'City parameter is missing'}), 400
    city = City.query.filter_by(id=city_id).first()
    if not city:
        return jsonify({'message': 'No city found'}), 404
    region = Region.query.filter_by(id=city.idRegion).first()
    return jsonify({'id': city.id, 'city': city.city, 'region': region.region})

@app.route('/cities', methods=['GET'])
@token_required
def cities(self):
    cities = City.query.all()
    if not cities:
        return jsonify({'message': 'no cities found'})
    cities_list = []
    for city in cities:
        region = Region.query.filter_by(id=city.idRegion).first()
        cities_list.append({'id': city.id, 'city': city.city, 'region': region.region})
    return jsonify(cities_list)