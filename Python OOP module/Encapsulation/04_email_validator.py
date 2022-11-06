import re


class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        search_pattern = r"([A-Za-z0-9]+)\@([a-z]+)\.([a-z]+)"
        result = re.match(search_pattern, email)
        name, mail, domain = result.groups()
        if not EmailValidator.__is_mail_valid(self, mail) \
                or not EmailValidator.__is_name_valid(self, name) \
                or not EmailValidator.__is_domain_valid(self, domain):
            return False

        return True


mails = ["gmail", "softuni"]

domains = ["com", "bg"]

email_validator = EmailValidator(6, mails, domains)

print(email_validator.validate("pe77er@gmail.com"))

print(email_validator.validate("georgios@gmail.net"))

print(email_validator.validate("stamatito@abv.net"))

print(email_validator.validate("abv@softuni.bg"))