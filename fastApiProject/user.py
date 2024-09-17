class user:
    def __init__(self, user_id, user_name, password, address, phone_number, city, country):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.address = address
        self.phone_number = phone_number
        self.city = city
        self.country = country

    def get_user_info(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "address": self.address,
            "phone_number": self.phone_number,
            "city": self.city,
            "country": self.country
        }