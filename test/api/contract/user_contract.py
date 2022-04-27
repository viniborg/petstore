import json
from faker import Faker


class Contract:

    def __init__(self) -> None:
        faker = Faker()
        self.contract = {
                "id": faker.random_number(fix_len=False),
                "username": faker.user_name(),
                "firstName": faker.first_name(),
                "lastName": faker.last_name(),
                "email": faker.email(),
                "password": faker.password(),
                "phone": faker.msisdn(),
                "userStatus": 0
            }

    def get(self, type: str = None):
        match type:
            case None:
                return json.dumps(self.contract)
            case "sucess":
                return json.dumps(self.contract)
            case "error_id":
                self.contract["id"] = 'Test'
                return json.dumps(self.contract)
            case "error_name":
                self.contract["username"] = ""
                return json.dumps(self.contract)
