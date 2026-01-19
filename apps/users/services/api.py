import requests
from datetime import datetime
from django.conf import settings

class RandomUserService:
    
    API_URL = settings.API_URL
    @classmethod
    def get_users(cls, results=10):
        response = requests.get(cls.API_URL, params={"results": results})
        
        response.raise_for_status()
        return response.json()["results"]
    
    @staticmethod
    def normalize_user(data):
        return {
            "name": f"{data['name']['first']} {data['name']['last']}",
            "gender": data["gender"][0].upper(),
            "location": f"{data['location']['city']}, {data['location']['country']}",
            "email": data["email"],
            "birthdate": datetime.fromisoformat(
                data["dob"]["date"].replace("Z", "")
            ).date(),
            "photo": data["picture"]["large"],
        }