import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds035006.mlab.com:35006/c4e22-poll

host = "ds035006.mlab.com"
port = 35006
db_name = "c4e22-poll"
user_name = "admin"
password = "1234@1234abH"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())