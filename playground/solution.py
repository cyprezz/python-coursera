import csv
import os

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = 'truck'
        self.body_length = float(0)
        self.body_width = float(0)
        self.body_height = float(0)
        self.parse_body_volume(self.body_whl)

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

    def parse_body_volume(self, body_whl):
        whl = body_whl.split("x")
        elements_count = len(whl)

        if elements_count == 3:
            if float(whl[0] and float(whl[1]) and float(whl[2])):
                self.body_length = float(whl[0])
                self.body_width = float(whl[1])
                self.body_height = float(whl[2])
            else:
                return None

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def validate_row(row):

    try:
        if row[0]:
            car_type = row[0]

            if not row[3] or str(row[3]).strip() == "" or not "." in row[3]:
                print(row[3], str(row[3]))
                raise ValueError
            if not row[1] or str(row[1]).strip() == "":
                print(row[1], str(row[1]))
                raise ValueError
            if not row[5] or not isinstance(float(row[5]), (int, float)):
                raise ValueError
            if car_type == 'car':
                if not row[2] or not int(row[2]):
                    raise ValueError
                if row[4] or row[6]:
                    raise ValueError
            if car_type == 'truck':
                if row[2] or row[6]:
                    raise ValueError
            if car_type == 'spec_machine':
                if row[2] or row[4]:
                    raise ValueError
                if not row[6] or str(row[6]).strip() == "":
                    raise ValueError
            return True
        else:
            raise ValueError
    except ValueError:
        return False
    except IndexError:
        return False


def get_car_list(csv_filename):
    with open(csv_filename) as csv_fd:
        car_list = []
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if validate_row(row):
                if row[0] == 'car':
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                elif row[0] == 'truck':
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif row[0] == 'spec_machine':
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
                else:
                    continue
    # print(car_list)
    return car_list
