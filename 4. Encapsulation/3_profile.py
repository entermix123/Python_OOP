class Profile:

    def __init__(self, username: str, password: str, ):     # initialize the class
        self.username = username            # set the username
        self.password = password            # set the password

    @property                               # getter of username
    def username(self):
        return self.__username

    @username.setter                        # setter of username
    def username(self, value):
        if not 5 <= len(value) <= 15:       # validate the username, must be more than 5 char and less than 15 chars
            raise ValueError("The username must be between 5 and 15 characters.")   # error if the username is not valid
        self.__username = value             # set the username if valid

    @property                               # getter of password
    def password(self):
        return self.__password

    @password.setter                        # setter of password
    def password(self, value):

        # validate the password: must be 8 chars at least, must contain at least 1 digit and 1 uppercase letter
        if len(value) < 8 or not any(x.isdigit() for x in value) or not any(k.isalpha() and k == k.upper() for k in value):

            # raise error if the password is not valid
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value             # set the password if valid

    def __str__(self):                      # return a string representation of the profile
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.__password)}"


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)


