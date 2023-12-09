from datetime import datetime, timedelta


def valid_profile(func):
    def wrapper(name, email, dob):
        try:
            # Check that dob s in the correct format (YYY-MM-DD)
            dob = datetime.strptime(dob, '%Y-%m-%d')

            # Check if user is at least 18 years old
            eighteen_years_ago = datetime.now() - timedelta(days=365 * 18)
            if dob > eighteen_years_ago:
                raise ValueError("You must be at least 18 years old to create an account")
        except ValueError as e:
            return str(e)

        # if do is valid call the original function with the arguments
        return func(name, email, dob)

    return wrapper


@valid_profile
def create_profile(name, email, dob):
    # code create user profile
    return "Profile created successfully"


result = create_profile("John", "dycjh@example.com", "1990-04-23")
result2 = create_profile("John", "dycjh@example.com", "2015-04-23")
print(result)
print(result2)
