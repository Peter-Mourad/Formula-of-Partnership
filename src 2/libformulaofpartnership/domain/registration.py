from pydantic import BaseModel
from libformulaofpartnership.domain import user, utils
import uuid


class Partner(BaseModel):
    first_name: str
    last_name: str
    email: str
    partner_code: str = None
    business_name: str = None

    def register(self):
        self.partner_code = str(uuid.uuid4())
        user.add_user(
            {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "business_name": self.business_name,
                "partner_code": self.partner_code,
                "is_approved": 0,
            }
        )
        return f"Thanks {self.first_name} for your registration, we will contact you through you phone number to proceed with registration"


def get_demo_user():
    defult_partner_code = "demo-11beae1a-4e25-404b-9aab-d2774bae712f"
    return utils.create_access_token(
        {
            "first_name": "Demo",
            "last_name": "Account",
            "email": "demo@demo.com",
            "business_name": "FakeCorp",
            "partner_code": defult_partner_code,
            "is_approved": 1,
        }
    )
