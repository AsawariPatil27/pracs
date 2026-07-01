import os
from db import users

def default_user(telegramId):
    return{
        "telegramId":str(telegramId),
        "language":"",
        "interactionMode":"",
        "incomeType":"",
        "occupation":"",
        "monthlyIncome":0,
        "monthlyExpense":0,
        "lowestMonthIncome":0,
        "state":"",
        "district":"",
        "harvestIncome":0,
        "leanDurationMonths":0,
        "leanMonthlyIncome":0,
        "currentStep":"start",
        "profileCompleted":False,
    }

def save_user(user):
    users.update_one({"telegramId": user["telegramId"]},{"$set":user},upsert=True)
    return user

def get_or_create_user(telegramId,username="",firstName=""):
    telegramId=str(telegramId)
    user=users.find_one({"telegramId":telegramId})
    if not user:
        user=default_user(telegramId)
        save_user(user)
        print("[NEW USER]",telegramId)
        return user
    
    user.pop("_id",None)
    return user