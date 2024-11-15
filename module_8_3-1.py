class IncorrectVinNumber(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers


        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):

        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):

        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера, строка должна состоять ровно из 6 символов')
        return True

    def get_info(self):

        return {
            'model': self.model,
            'vin': self.__vin,
            'numbers': self.__numbers
        }


try:
    car = Car(model="Toyota Camry", vin=1234567, numbers="ABC123")
    print(car.get_info())
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(f"Ошибка: {e.message}")