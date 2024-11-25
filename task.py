#QUESTION NO:1,2,3

class Circle:
    def __init__(self, radius_list):
        self.__radius_list = radius_list  
        self.__pi = 3.141 
        
    def calculate_areas(self):
        areas = []
        for radius in self.__radius_list:
            area = self.__pi * radius**2
            areas.append(area)
        return areas

   
    def calculate_perimeters(self):
        perimeters = []
        for radius in self.__radius_list:
            perimeter = 2 * self.__pi * radius
            perimeters.append(perimeter)
        return perimeters



if __name__ == "__main__":
    radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
    circle = Circle(radius_list)

    areas = circle.calculate_areas()
    print("Areas:", areas)

    perimeters = circle.calculate_perimeters()
    print("Perimeters:", perimeters)
