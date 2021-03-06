# self.public
# self._protected
# self.__private


class everythingThatDrives:
    def __init__(self, driverName, location, id):
        self.driverName = driverName
        self.location = location    # Tupel Long, Lat
        self.id = id
        print("driverName: ", driverName, " location: ",
              location, " id: ", id)

    def updateValues(self, driverName=None, location=None, isFree=None):
        if driverName != None:                  # Prevents the values from beeing overridden with none
            self.driverName = driverName
        if location != None:
            self.location = location            # Tupel Long, Lat
        if isFree != None:
            self.isFree = isFree


class Ambulance(everythingThatDrives):
    def __init__(self, driverName, location, isFree, id):
        super().__init__(driverName, location, id)
        self.isFree = isFree
        print("New Ambulance generated!")


class Firefighter(everythingThatDrives):
    def __init__(self, driverName, location, isFree, id):
        super().__init__(driverName, location, id)
        self.isFree = isFree
        print("New Firefighter generated!")


class Police(everythingThatDrives):
    def __init__(self, driverName, location, isFree, id):
        super().__init__(driverName, location,  id)
        self.isFree = isFree
        print("New Police generated!")


class userCar(everythingThatDrives):
    def __init__(self, driverName, location, reasons, id):
        super().__init__(driverName, location,  id)
        self.reasons = reasons
        print("New userCar generated!")


class Hospital:
    def __init__(self, hospitalName, location, doctors, id, freeRooms, specialists):
        self.hospitalName = hospitalName
        self.location = location        # Tupel Long, Lat
        self.doctors = doctors          # list
        self.specialists = specialists  # list
        self.freeRooms = freeRooms      # int
        self.id = id                    # string
        print("New Hospital generated!")
        print("HospitalName: ", hospitalName, " location: ",
              location, " Doctors: ", doctors, " id: ", id, " freeRooms: ", freeRooms, " specialists: ", specialists)

    def updateValues(self, hospitalName=None, location=None, doctors=None, specialists=None, freeRooms=None, id=None):
        if hospitalName != None:
            self.hospitalName = hospitalName
        if doctors != None:
            self.doctors = doctors          # list
        if specialists != None:
            self.specialists = specialists  # list
        if freeRooms != None:
            self.freeRooms = freeRooms
