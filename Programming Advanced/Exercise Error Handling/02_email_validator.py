import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


search_pattern = r'(\w+)\@(\w+)(.\w{1,})'
valid_domains = [".com", ".bg", ".net", ".org"]

while True:
    command = input()
    if command == "End":
        break

    current_email = command

    if "@" not in current_email:
        raise MustContainAtSymbolError("Email must contain @")

    result = re.search(search_pattern, current_email)

    if result:
        name = result.group(1)
        domain = result.group(3)

        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        elif domain not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        print("Email is valid")
