class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):   # initialize with list of mails and domains
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str):       # validate length of name
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str):       # check if mail is in list of mails
        return mail in self.mails               # boolean result True/False

    def __is_domain_valid(self, domain: str):   # check if domain is in list of domains
        return domain in self.domains           # boolean result True/False

    def validate(self, email: str):             # validate email
        name, rest = email.split('@')           # split email by '@' symbol
        mail, domain = rest.split('.')          # split email and domain by '.' symbol

        # validate name, mail and domain
        if self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True
        else:
            return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
