class Person:
    nationality = "Uzbekistan"
    def __init__(self, name, lastname, age, sex):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.sex = sex


class Cutomer(Person):
    def __init__(self, name, lastname, age, sex, is_married, has_real_estate, trustee_number, work_place, org_type, salary, spent_money_per_month):
        super().__init__(name, lastname, age, sex)
        self.is_married = is_married
        self.has_real_estate = has_real_estate
        self.trustee_number = trustee_number
        self.work_place = work_place
        self.org_type = org_type
        self.salary = salary
        self.spent_money_per_month = spent_money_per_month

    def request_loan(self, bank, loan_money, duration_months, payment_date):
        pass

    def sign_loan(self):
        pass


class Bank:
    def __init__(self, name, min_limit, max_limit, min_interest, max_interest, min_duration, max_duration):
        self.name = name
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.min_interest = min_interest
        self.max_interest = max_interest
        self.min_duration = min_duration
        self.max_duration = max_duration


    # ! Метод, который запрашивает у КАБ кредитный рейтинг клиента
    def request_customer_rating():
        pass
    
    # ? Метод, который считает условия выдаваемого кредита
    def calculate_loan():
        pass

    # * Метод, который выдаёт кредит
    def sign_loan():
        pass

class CreditBureau:
    def calculate_rating():
        # 1. Наличие кредитов
        # 2. Наличие просрочек
        # 3. Успешно закрытые кредиты
        pass