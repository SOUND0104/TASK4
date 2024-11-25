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



# question 4
class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.channel = 1
        self.price = price
        self.inches = inches
        self.on_off_status = False
        self.volume = 50


    def power_toggle(self):
        self.on_off_status = not self.on_off_status
        return "TV is now ON" if self.on_off_status else "TV is now OFF"


    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
        return f"Volume: {self.volume}"


    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        return f"Volume: {self.volume}"


    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
        return f"Channel: {self.channel}"


    def reset_tv(self):
        self.channel = 1
        self.volume = 50
        return "TV reset to channel 1 and volume 50"


    def status(self):
        on_off = "ON" if self.on_off_status else "OFF"
        return f"{self.brand} TV is {on_off} at channel {self.channel}, volume {self.volume}"


class LedTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return (f"{self.brand} LED TV Details:\n"
                f"Inches: {self.inches}, Price: ${self.price}, Screen Thickness: {self.screen_thickness} mm, "
                f"Energy Usage: {self.energy_usage} W, Lifespan: {self.lifespan} hours, "
                f"Refresh Rate: {self.refresh_rate} Hz, Viewing Angle: Excellent, Backlight: LED")


class PlasmaTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return (f"{self.brand} Plasma TV Details:\n"
                f"Inches: {self.inches}, Price: ${self.price}, Screen Thickness: {self.screen_thickness} mm, "
                f"Energy Usage: {self.energy_usage} W, Lifespan: {self.lifespan} hours, "
                f"Refresh Rate: {self.refresh_rate} Hz, Viewing Angle: Good, Backlight: Plasma")



if __name__ == "__main__":

    tv = TV("Panasonic", 400, 42)
    print(tv.status())
    print(tv.power_toggle())
    print(tv.increase_volume())
    print(tv.set_channel(45))
    print(tv.reset_tv())
    print(tv.status())

  
    led_tv = LedTV("Samsung", 800, 55, 10, 120, 50000, 120)
    print(led_tv.status())
    print(led_tv.display_details())

    plasma_tv = PlasmaTV("LG", 700, 50, 20, 200, 30000, 60)
    print(plasma_tv.status())
    print(plasma_tv.display_details())


