'''
TELEVISION REMOTE CONTROL

The volume has to be between 0 and 10
the channel between 1 and 50
if the television is off the other buttons are off also
buttons: power, mute, volume up, volume down, channel up, channel down, setting, get info

Made by Alessandro Silvestri - 2023 <alessandro.silvestri.work@gmail.com>
'''

from dimmer_switch import Dimmer_switch

class Television(Dimmer_switch):
    def __init__(self):
        self.is_power_on = False
        self.is_mute_on = False
        self.volume = 0
        self.channel = 1
        super().__init__() # I take all the values from Dimmer_switch class

    def get_info(self):
        '''print all the television values, at the end the dim values'''
        print("Power: ",self.is_power_on)
        print("Mute: ", self.is_mute_on)
        print("Volume: ", self.volume)
        print("Channel: ", self.channel)
        self.dim_display() # here I use the method of the class Dimmer_switch

    def power(self):
        '''button power on'''
        self.is_power_on = not self.is_power_on
        if not self.is_power_on: # if the TV is off all the values return to the default
            self.is_mute_on = False
            self.volume = 0
            self.channel = 1
            self.dim_power = False
            self.dim_brightness = 0

    def mute(self):
        if not self.is_power_on: return # if the TV is off you can't change the values
        '''button mute'''
        self.is_mute_on = not self.is_mute_on

    def volume_up(self):
        '''button volume up, not more than 10'''
        if not self.is_power_on: return # if the TV is off you can't change the values
        self.volume += 1
        if self.volume > 10:
            self.volume = 10
    
    def volume_down(self):
        if not self.is_power_on: return # if the TV is off you can't change the values
        '''button volume down it can't go under 0'''
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
    
    def channel_up(self):
        if not self.is_power_on: return # if the TV is off you can't change the values
        '''button channel up not more than 50'''
        self.channel += 1
        if self.channel > 50:
            self.channel = 50
    
    def channel_down(self):
        if not self.is_power_on: return # if the TV is off you can't change the values
        '''button channel down, it can't go under 1'''
        self.channel -= 1
        if self.channel < 1:
            self.channel = 1

    def channel_set(self, num: int):
        '''buttons setting the channels, it can't go under 1'''
        if not self.is_power_on: return # if the TV is off you can't change the values
        self.channel = num
        if self.channel < 1:
            self.channel = 1


########### Using the object ###########
my_tv = Television()
my_tv2 = Television()

# using the dimmer on the remote control
my_tv.dim_power_button()
my_tv.dim_rise_level()
my_tv.dim_rise_level()
my_tv.dim_rise_level()

# using the remote control
my_tv.power() # here I turn on the TV
my_tv.channel_set(5)
my_tv.channel_up()
my_tv.volume_up()
my_tv.volume_up()
my_tv.volume_up()
my_tv.get_info()
#################################


#### using the second object####
my_tv2.get_info()
###############################
