class Dough:

    def __init__(self, flour_type: str, baking_technique: str, weight: float):  # initializes a Dough object
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property                       # create getter method for flour_type
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter                  # setter method for flour_type
    def flour_type(self, value):
        if value == '':                 # check if value is an empty string
            raise ValueError("The flour type cannot be an empty string")    # if it's an empty string, raise an error
        self.__flour_type = value       # if it's not an empty string, set the value of the flour_type
    
    @property                           # create getter method for baking_technique
    def baking_technique(self):
        return self.__baking_technique
    
    @baking_technique.setter            # setter method for baking_technique
    def baking_technique(self, value):
        if value == '':                 # check if value is an empty string
            raise ValueError("The baking technique cannot be an empty string")  # if it's an empty string, raise an error
        self.__baking_technique = value     # if it's not an empty string, set the value of the baking_technique
    
    @property                           # getter method for weight
    def weight(self):
        return self.__weight
    
    @weight.setter                      # setter method for weight
    def weight(self, value):
        if value <= 0:           # check if value is less than zero
            raise ValueError("The weight cannot be less or equal to zero")  # if it's less than zero, raise an error
        self.__weight = value       # if it's not less than zero, set the value of the weight
