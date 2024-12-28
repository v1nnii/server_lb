import json

# Класс Тарифа
class Tariff:
    def __init__(self, name, monthly_fee, data_limit, clients_count):
        self.name = name
        self.monthly_fee = monthly_fee
        self.data_limit = data_limit
        self.clients_count = clients_count

    def __str__(self):
        return f"Тариф: {self.name}, Ежемесечная плата: {self.monthly_fee}, GB: {self.data_limit}GB, Клиентов: {self.clients_count}"

# Класс мобильной компании
class MobileCompany:
    def __init__(self, name):
        self.name = name
        self.tariffs = []

    # Добавление тарифа
    def add_tariff(self, tariff):
        self.tariffs.append(tariff)

    # Подсчет общего числа клиентов
    def total_clients(self):
        return sum(tariff.clients_count for tariff in self.tariffs)

    # Сортировка по абонентской плате
    def sort_tariffs_by_fee(self):
        self.tariffs.sort(key=lambda tariff: tariff.monthly_fee)

    # Поиск тарифа по заданному диапазону абонентской платы
    def find_tariff_by_fee_range(self, min_fee, max_fee):
        return [tariff for tariff in self.tariffs if min_fee <= tariff.monthly_fee <= max_fee]

    # Загрузка данных о тарифах из файла
    def load_tariffs(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                tariff = Tariff(item['name'], item['monthly_fee'], item['data_limit'], item['clients_count'])
                self.add_tariff(tariff)

    # Сохранение данных о тарифах в файл
    def save_tariffs(self, file_path):
        data = [{'name': tariff.name, 'monthly_fee': tariff.monthly_fee, 'data_limit': tariff.data_limit, 'clients_count': tariff.clients_count}
                for tariff in self.tariffs]
        with open(file_path, 'w') as file:
            json.dump(data, file)

# Создание консольного меню
def console_menu(company):
    while True:
        print("\n1. Добавить тариф")
        print("2. Показать все тарифы")
        print("3. Подсчитать общее количество клиентов")
        print("4. Отсортировать тарифы по абонентской плате")
        print("5. Найти тариф по диапазону абонентской платы")
        print("6. Загрузить тарифы из файла")
        print("7. Сохранить тарифы в файл")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Название тарифа: ")
            monthly_fee = float(input("Абонентская плата: "))
            data_limit = float(input("Лимит данных (в GB): "))
            clients_count = int(input("Количество клиентов: "))
            tariff = Tariff(name, monthly_fee, data_limit, clients_count)
            company.add_tariff(tariff)

        elif choice == '2':
            for tariff in company.tariffs:
                print(tariff)

        elif choice == '3':
            print("Общее количество клиентов:", company.total_clients())

        elif choice == '4':
            company.sort_tariffs_by_fee()
            print("Тарифы отсортированы.")

        elif choice == '5':
            min_fee = float(input("Минимальная абонентская плата: "))
            max_fee = float(input("Максимальная абонентская плата: "))
            tariffs = company.find_tariff_by_fee_range(min_fee, max_fee)
            for tariff in tariffs:
                print(tariff)

        elif choice == '6':
            file_path = input("Введите путь к файлу для загрузки: ")
            company.load_tariffs(file_path)
            print("Тарифы загружены.")

        elif choice == '7':
            file_path = input("Введите путь к файлу для сохранения: ")
            company.save_tariffs(file_path)
            print("Тарифы сохранены.")

        elif choice == '0':
            break

        else:
            print("Неверный выбор")

# Основная часть программы
if __name__ == "__main__":
    company = MobileCompany("My Mobile Company")
    console_menu(company)
