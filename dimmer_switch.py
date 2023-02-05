'''
DIMMER SWITCH
feautures: Turn on / off, Raise level, Lower level, Show values
'''

class Dimmer_switch():
    def __init__(self):
        self.power = False
        self.brightness = 0
    
    def power_button(self):
        '''on/off button'''
        self.power = not self.power
        if not self.power:
            self.brightness = 0

    def rise_level(self):
        '''increase the brightness of 1 if power is on'''
        if self.power:
            self.brightness += 1
            if self.brightness > 10:
                self.brightness = 10

    def lower_level(self):
        '''lower the brightness of 1 if power is on'''
        if self.power:
            self.brightness -= 1
            if self.brightness < 0:
                self.brightness = 0

    def display(self):
        '''display the values: power and brightness'''
        print(f'''
        power: {self.power}
        brightness level: {self.brightness}
        ''')

# using the object
my_dimmer = Dimmer_switch()
my_dimmer.rise_level()
my_dimmer.display()
