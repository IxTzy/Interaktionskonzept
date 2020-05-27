def checkNadd(id, list, obj, split, location):
    if len(list) == 0:
        list.append(
            obj(split[0], location, split[2], split[3]))
        return True

    else:
        for x in range(0, len(list)):
            if str(list[x].id) == str(id):
                print("There is an entity with the same id: ", id)
                return False

        list.append(
            obj(split[0], location, split[2], split[3]))
        return True


def compareNupdate(message, data, location, List):
    topic = message[2]
    id = message[3]

    if topic == "ambulances":
        entity = findEntity(List[1], id, data)
        print(entity.id)
    elif topic == "firefighters":
        entity = findEntity(List[0], id, data)
        print(entity.id)
        update(topic, entity, data)
    elif topic == "polices":
        entity = findEntity(List[2], id, data)
        print(entity.id)
    elif topic == "hospitals":
        entity = findEntity(List[4], id, data)
        print(entity.id)
    elif topic == "users":
        entity = findEntity(List[3], id, data)
        print(entity.id)
    pass


def findEntity(List, id, data):
    if data[3] != id:
        print("Id does not Match Topic Id! Topic: ", id, "Id: ", data[3])
        return False
    else:
        try:
            entity = next((x for x in List if x.id == id), None)
            print("Found an Entity!")
            pass
        except Exception as e:
            print(e)
            raise
        return entity


def update(topic, entity, data):
    if topic == "hospital":
        print("hospital routine follows........")
    elif topic == "users":
        print("users routine follows........")
    else:
        # set the new values for pol, amb and firefighters
        try:
            print(data[2])
            print(type(data[2]))
            entity.updateValues(
                driverName=data[0], location=data[1], isFree=data[2])
            pass
        except Exception as e:
            print(e)
            raise
