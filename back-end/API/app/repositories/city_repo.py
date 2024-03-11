from app.models.city_model import City
from app.models.region_model import Region

class CityRepo:

        def city(self, data):
            city = City.query.filter_by(city=data['city']).first()
            if not city:
                return
            return city
    
        def cities(self):
            cities = City.query.all()
            return cities