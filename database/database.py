#(©)CodeXBotz




import pymongo, os
from config import DB_URI, DB_NAME


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database['users']



async def del_channelis():
    Channel_List_No = 1
    x = user_data.find_one_and_delete({'Channel_List_No':str(Channel_List_No)})
    if x is not None:
        check = "Fine"
    else:
        check = None
    return check

async def set_channelis(Channel_List):
    Channel_List_No = 1
    x = user_data.update_one({'Channel_List_No':str(Channel_List_No)},{'$set': {'Channel_List': Channel_List}},upsert=True)
    #print("Result --->",x)
    return x


async def get_channelis():
    Channel_List_No = 1
    x = user_data.find_one({'Channel_List_No':str(Channel_List_No)})
    #print("X1 is Here ---->",x)
    if x is not None:
        #print("X is Here ---->",x)
        check = x['Channel_List']
        #print("Yoooo----->",check) 
    else:
        check = None
    return check





async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    if found:
        return True
    else:
        return False

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return
