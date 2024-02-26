from app.repositories.city_repo import CityRepo
city_repo = CityRepo()

class CityService:
    def getCity(self, data):
        return city_repo.getCity(data)
    
    def getAllCities(self):
        return city_repo.getAllCities()