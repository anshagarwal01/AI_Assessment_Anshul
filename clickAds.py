from pydantic import BaseModel


# 2. Class which describes Click Ads measurements
class ClickAd(BaseModel):
    TimeSpent: float
    Age: int
    AreaIncome: float
    InternetUsage: float
    Male: int


