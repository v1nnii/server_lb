class Customer:
    def __init__(self, id, last_name, first_name, middle_name, address, credit_card_number, bank_account_number):
        # Основной конструктор
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.credit_card_number = credit_card_number
        self.bank_account_number = bank_account_number

    @classmethod
    def from_full_name(cls, id, full_name, address, credit_card_number, bank_account_number):
        # Разделяем полное имя на части
        names = full_name.split(' ')
        if len(names) == 3:
            last_name, first_name, middle_name = names
        elif len(names) == 2:
            last_name, first_name = names
            middle_name = ''
        else:
            raise ValueError("Invalid full name format")
        return cls(id, last_name, first_name, middle_name, address, credit_card_number, bank_account_number)

    def getTun(self):
        return self.id, self.last_name, self.first_name, self.middle_name, self.address, self.credit_card_number, self.bank_account_number

    def setTun(self, id=None, last_name=None, first_name=None, middle_name=None, address=None, credit_card_number=None, bank_account_number=None):
        if id is not None:
            self.id = id
        if last_name is not None:
            self.last_name = last_name
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if address is not None:
            self.address = address
        if credit_card_number is not None:
            self.credit_card_number = credit_card_number
        if bank_account_number is not None:
            self.bank_account_number = bank_account_number

  
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}, Address: {self.address}, Credit Card: {self.credit_card_number}, Bank Account: {self.bank_account_number}"

    
    def __hash__(self):
        return hash((self.id, self.credit_card_number, self.bank_account_number))

   
    def __eq__(self, other):
        if isinstance(other, Customer):
            return (self.id == other.id and
                    self.credit_card_number == other.credit_card_number and
                    self.bank_account_number == other.bank_account_number)
        return False


def print_customers_sorted_by_name(customers):
    sorted_customers = sorted(customers, key=lambda customer: (customer.last_name, customer.first_name))
    for customer in sorted_customers:
        print(customer)


def print_customers_by_credit_card_interval(customers, min_card, max_card):
    filtered_customers = [customer for customer in customers if min_card <= customer.credit_card_number <= max_card]
    for customer in filtered_customers:
        print(customer)

if __name__ == "__main__":
    customers = [
        Customer(1, "Иванов", "Иван", "Иванович", "ул. Ленина, д.1", 1234567890123456, 1111111111),
        Customer(2, "Петров", "Петр", "Петрович", "ул. Гагарина, д.5", 2345678901234567, 2222222222),
        Customer(3, "Сидоров", "Сидор", "Сидорович", "ул. Советская, д.10", 3456789012345678, 3333333333),
    ]

    print("A) Список покупателей в алфавитном порядке:")
    print_customers_sorted_by_name(customers)

    print("\nB) Список покупателей с номерами кредитных карт в интервале [2000000000000000, 3500000000000000]:")
    print_customers_by_credit_card_interval(customers, 2000000000000000, 3500000000000000)
