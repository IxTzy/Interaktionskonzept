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
