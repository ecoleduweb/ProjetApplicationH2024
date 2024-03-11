from app.repositories.city_repo import CityRepo
city_repo = CityRepo()

class CityService:
    def city(self, data):
        return city_repo.city(data)
    
    def cities(self):
        return city_repo.cities()