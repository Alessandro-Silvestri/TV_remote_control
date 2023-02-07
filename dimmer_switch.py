'''
DIMMER SWITCH
Class representation of a Dimmer.
features: Turn on / off, Raise level, Lower level, Show values
Made by Alessandro Silvestri - 2023 <alessandro.silvestri.work@gmail.com>
'''

class Dimmer_switch():
    def __init__(self):
        self.dim_power = False
        self.dim_brightness = 0
    
    def dim_power_button(self):
        '''on/off button'''
        self.dim_power = not self.dim_power
        if not self.dim_power:
            self.dim_brightness = 0

    def dim_rise_level(self):
        '''increase the brightness of 1 if power is on'''
        if self.dim_power:
            self.dim_brightness += 1
            if self.dim_brightness > 10:
                self.dim_brightness = 10

    def dim_lower_level(self):
        '''lower the brightness of 1 if power is on'''
        if self.dim_power:
            self.dim_brightness -= 1
            if self.dim_brightness < 0:
                self.dim_brightness = 0

    def dim_display(self):
        '''display the values: power and brightness'''
        print(f'''
        dimmer power: {self.dim_power}
        dimmer brightness level: {self.dim_brightness}
        ''')

# using the object
# my_dimmer = Dimmer_switch()
# my_dimmer.dim_power_button()
# my_dimmer.dim_display()
