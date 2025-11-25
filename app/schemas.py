from pydantic import BaseModel

class CustomerFeatures(BaseModel):
    State: str
    Account_length: int
    Area_code: int
    International_plan: str
    Voice_mail_plan: str
    Number_vmail_messages: int
    Total_day_minutes: float
    Total_day_calls: int
    Total_day_charge: float
    Total_eve_minutes: float
    Total_eve_calls: int
    Total_eve_charge: float
    Total_night_minutes: float
    Total_night_calls: int
    Total_night_charge: float
    Total_intl_minutes: float
    Total_intl_calls: int
    Total_intl_charge: float
    Customer_service_calls: int
