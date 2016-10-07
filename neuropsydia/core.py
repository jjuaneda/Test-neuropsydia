# -*- coding: utf-8 -*-
from .screen import screen, screen_width, screen_height

import os
import pygame
import time as builtin_time


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
class Time():
    """
    A class object to wait some time, get time, control time and such.
    Its methods (functions) are:
        - reset()
        - control()
        - wait()
    See those for further informations.

    Note that by default, there is already a Time class object called "time"      (lowercase) that is initialized at neuropsydia loading. To improve clarity, use this one (e.g., n.time.wait() ), especially for wait() and control() functions.

    Parameters
    ----------
    None

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> myclock = n.Time()
    >>> time_passed_since_myclock_creation = myclock.get()
    >>> myclock.reset()
    >>> time_passed_since_reset = myclock.get()
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    - time
    """
    def __init__(self):
        self.clock = builtin_time.clock()
        self.pygame_clock = pygame.time.Clock()

    def reset(self):
        """
        Reset the clock of the Time object.

        Parameters
        ----------
        None

        Returns
        ----------
        None

        Example
        ----------
        >>> import neuropsydia as n
        >>> n.start()
        >>> time_passed_since_neuropsydia_loading = n.time.get()
        >>> n.time.reset()
        >>> time_passed_since_reset = n.time.get()
        >>> n.close()

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - pygame 1.9.2
        - time
        """
        self.clock = builtin_time.clock()
        self.pygame_clock = pygame.time.Clock()

    def control(self, frequency=60):
        """
        Control time. Must be placed in a while loop and, each time the program runs through it, checks if the time passed is less than a certain amount (the frequency, by default 60, so 1/60 seconds). If true, the program stops and wait what needed before continuing, so that each loop takes at least 1/frequency seconds to be complete.

        Parameters
        ----------
        frequency = int, optional
            The minimum frequency you want the loop to run at

        Returns
        ----------
        None

        Example
        ----------
        >>> import neuropsydia as n
        >>> n.start()
        >>> while n.time.get() < 5:
        >>>     n.time.control()
        >>>     print(n.time.get())
        >>> n.close()

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - pygame 1.9.2
        - time
        """
        self.pygame_clock.tick_busy_loop(frequency)

    def get(self, reset=True):
        """
        Get time since last initialisation / reset.

        Parameters
        ----------
        reset = bool, optional
            Should the clock be reset after returning time?

        Returns
        ----------
        float
            Time passed in milliseconds.

        Example
        ----------
        >>> import neuropsydia as n
        >>> n.start()
        >>> time_passed_since_neuropsydia_loading = n.time.get()
        >>> n.time.reset()
        >>> time_passed_since_reset = n.time.get()
        >>> n.close()

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - pygame 1.9.2
        - time
        """
        t = (builtin_time.clock()-self.clock)*1000

        if reset is True:
            self.reset()
        return(t)

    def wait(self, time_to_wait, unit="ms", frequency=60, round_by_frame=True, skip=None):
        """
        Wait some time.

        Parameters
        ----------
        time_to_wait = int
            Time to wait
        unit = str
            "min" for minutes, "s" for seconds, "ms" for milliseconds, or "frame" for a certain amount of frames (depending on the frequency parameter)
        frequency = int
            should be a multiple of your monitor's refresh rate
        round by frame = bool
            should the waiting time be rounded to match an exact number of frame / refresh cycles? (e.g., on a 60Hz monitor, 95ms will be rounded to 100, because the monitor is refreshed every 16.6667ms)
        skip = str
            Shoud there be a key to skip the waiting. Default to None.

        Returns
        ----------
        float
            Actual time waited in milliseconds

        Example
        ----------
        >>> import neuropsydia as n
        >>> n.start()

        >>> n.write("let's wait 500ms", round_by_frame = False)
        >>> n.refresh()
        >>> wait_time = n.time.wait(520)
        >>> n.background_color("white")
        >>> n.write("I waited for " + str(wait_time) + "ms")
        >>> n.refresh()
        >>> wait_time = n.time.wait(520, round_by_frame = True)
        >>> n.background_color("white")
        >>> n.write("I waited for " + str(wait_time) + "ms")
        >>> n.refresh()
        >>> n.time.wait(3, unit = "s")

        >>> n.close()

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - pygame 1.9.2
        - time
        """
        t0 = builtin_time.clock()
        if unit == "min":
            time_to_wait = time_to_wait * 60
            unit = "s"
        if unit == "s":
            time_to_wait = time_to_wait * 1000
            unit = "ms"
        if unit == "ms":
            if round_by_frame is True:
                time_to_wait = round(time_to_wait / (1/frequency*1000))
                time_to_wait = round(time_to_wait * (1/frequency*1000))
        if unit == "frame":
            time_to_wait = time_to_wait * (1/frequency*1000)

        if skip is None:
            pygame.time.delay(time_to_wait)  # In milliseconds
        else:
            response(allow=skip, time_max=time_to_wait)
        return((builtin_time.clock()-t0)*1000)
time = Time()

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================


def background_color(color_name="white", opacity=100, fade=False, fade_speed=60, fade_type="out", auto_refresh=False):
    """
    Fill the background with a color.

    Parameters
    ----------
    color_name = str, tuple, optional
        name of the color (see color() function), or an RGB tuple (e.g., (122,84,01))
    opacity = int, optional
        opacity of the color (in percents)
    fade = bool, optional
        do you want a fade effect?
    fade_speed = int, optional
        frequency (speed) of the fading
    fade_type = str, optional
        "out" or "in", fade out or fade in

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.background_color("blue")
    >>> n.refresh()
    >>> n.time.wait(500)
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    - time
    """
    if color_name is not None:
        if fade is False:
            if opacity == 100:
                try:
                    screen.fill(color(color_name))
                except:
                    print("NEUROPSYDIA ERROR: background_color(): wrong argument")
            else:
                opacity = int(opacity * 255 / 100)
                color_name = color(color_name) + (opacity,)
                mask = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)  # per-pixel alpha
                mask.fill(color_name)  # notice the alpha value in the color
                screen.blit(mask, (0, 0))
            if auto_refresh is True:
                refresh()
        if fade is True:
            original_color_name = color_name
            clock = pygame.time.Clock()
            for i in range(0, 40, 1):
                clock.tick_busy_loop(fade_speed)
                if fade_type == "out":
                    color_name = color(original_color_name) + (i,)
                else:
                    color_name = color(original_color_name) + (255-i, )
                mask = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)  # per-pixel alpha
                mask.fill(color_name)  # notice the alpha value in the color
                screen.blit(mask, (0, 0))
                refresh()
            screen.fill(color(original_color_name))


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def refresh():
    """
    Reresh / flip the screen, actually display things on screen (to use after image(), write() or background_color()).

    Parameters
    ----------
    None

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.background_color("blue")
    >>> n.refresh()
    >>> n.time.wait(500)
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    """
    pygame.display.flip()

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
keys = {
"normal":
    {109: ',', 44: ';', 46: ':',47: '!', 97: 'q',
     98: 'b', 99: 'c', 100: 'd', 101: 'e',
     102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j',
     107: 'k', 108: 'l', 59: 'm', 110: 'n', 111: 'o',
     112: 'p', 113: 'a', 114: 'r', 115: 's', 116: 't',
     117: 'u', 118: 'v', 119: 'z', 120: 'x', 121: 'y',
     122: 'w', 57: 'ç', 56: '_', 55: 'è', 54: '-', 53: '(',
     52: "_", 51: '_', 50:'é', 49: '&', 48: 'à', 32: '_',
     13: "ENTER",276: "LEFT",274: "DOWN",275: "RIGHT",273: "UP",
     pygame.K_KP0: '0', pygame.K_KP1: '1', pygame.K_KP2: '2', pygame.K_KP3: '3',pygame.K_KP4: '4', pygame.K_KP5: '5',pygame.K_KP6: '6',pygame.K_KP7: '7',pygame.K_KP8: '8',pygame.K_KP9: '9'},

"shift":
    {109:'?', 44: '.', 46: '/',47: '§', 97: 'Q',
     98: 'B', 99: 'C', 100: 'D', 101 : 'E',
     102: 'F', 103: 'G', 104: 'H', 105: 'I', 106: 'J',
     107: 'K', 108: 'L', 59: 'M', 110: 'N', 111: 'O',
     112: 'P', 113: 'A', 114: 'R', 115: 'S', 116: 'T',
     117: 'U', 118: 'V', 119: 'Z', 120: 'X', 121: 'Y',
     122: 'W', 57: '9', 56: '8', 55: '7', 54: '6', 53: '5',
     52: '4', 51: '3', 50: '2', 49: '1', 48: '0', 32: '_',
     13: "ENTER",276: "LEFT",274: "DOWN",275: "RIGHT",273: "UP",
     pygame.K_KP0: '0',pygame.K_KP1: '1',pygame.K_KP2: '2',pygame.K_KP3:'3',pygame.K_KP4: '4',
     pygame.K_KP5: '5',pygame.K_KP6: '6',pygame.K_KP7: '7',pygame.K_KP8: '8',pygame.K_KP9:'9'},

"altgr":
    {97: 'q', 98: 'b', 99: 'c', 100: 'd', 101 : '€',
     102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j',
     107: 'k', 108: 'l', 59: 'm', 110: 'n', 111: 'o',
     112: 'p', 113: 'a', 114: 'r', 115: 's', 116: 't',
     117: 'u', 118: 'v', 119: 'z', 120: 'x', 121: 'y',
     122: 'w', 57: '^', 56: '_', 55: '`', 54: '|', 53: '[',
     52: '{', 51: '#', 50: '~', 49: '1', 48: '@', 32: '_',
     13: "ENTER",276: "LEFT",274: "DOWN",275: "RIGHT",273: "UP",
     pygame.K_KP0: '0',pygame.K_KP1: '1',pygame.K_KP2: '2',pygame.K_KP3: '3',pygame.K_KP4: '4',
     pygame.K_KP5: '5',pygame.K_KP6: '6',pygame.K_KP7: '7',pygame.K_KP8: '8',pygame.K_KP9: '9'}
}


def wait_for_input(time_max=None):
    if pygame.event.get_blocked(pygame.KEYDOWN) is True:
        blocked = True
        pygame.event.set_allowed(pygame.KEYDOWN)
    else:
        blocked = False
        pygame.event.set_allowed(pygame.KEYDOWN)

    time_out = False
    loop = True
    if time_max is None:
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        modifier = "shift"
                    elif pygame.key.get_mods() & pygame.KMOD_RALT:
                        modifier = "altgr"
                    else:
                        modifier = "normal"
                    if event.key != pygame.K_RSHIFT and event.key != pygame.K_LSHIFT and event.key != pygame.K_RALT:
                        loop = False
    else:
        local_time = Time()
        while loop and local_time.get(reset=False) < time_max:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        modifier = "shift"
                    elif pygame.key.get_mods() & pygame.KMOD_RALT:
                        modifier = "altgr"
                    else:
                        modifier = "normal"
                    if event.key != pygame.K_RSHIFT and event.key != pygame.K_LSHIFT and event.key != pygame.K_RALT:
                        loop = False
        if local_time.get(reset=False) > time_max:
            time_out = True


    if blocked is True:
        pygame.event.set_blocked(pygame.KEYDOWN)

    if time_out == True:
        return("Time_Max_Exceeded")
    else:
        try:
            return(keys[modifier][event.key])
        except KeyError:
            return(event.key)


def response(allow=None, enable_escape=True, time_max=None, get_RT=True):
    """
    Get a (keyboard, for now) response.

    Parameters
    ----------
    allow = str or list
        keys to allow
    enable_escape = bool
        enable escape to exit
    time_max = int
        maximum time to wait for a response (ms)
    get_RT = bool
        return response time

    Returns
    ----------
    str or (str, int)
        returns a tuple when get_RT is set to True
    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    - time
    """
    local_time = Time()
    if allow is not None:
        if not isinstance(allow, list):
            allow = [allow]

    while True:
        pressed_key = wait_for_input(time_max=time_max)
        if pressed_key == "Time_Max_Exceeded":
            return("Time_Max_Exceeded", local_time.get())
        if pressed_key == pygame.K_ESCAPE:
            if enable_escape is True:
                if get_RT is True:
                    return("ESCAPE", local_time.get())
                else:
                    return("ESCAPE")
        elif allow is not None:
            if pressed_key in allow:
                if get_RT is True:
                    return(pressed_key, local_time.get())
                else:
                    return(pressed_key)
        else:
            if get_RT is True:
                return(pressed_key, local_time.get())
            else:
                return(pressed_key)

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
class Coordinates:
    """
    A class object to go from pygame corrdinates system to neuropsydia's and vice versa.

    Its methods (functions) are:
        - to_pygame()
        - from_pygame()

    Parameters
    ----------
    None

    Returns
    ----------
    None

    Example
    ----------
    None

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    """
    def to_pygame(x=None,y=None, distance_x=None, distance_y=None):
        """
        Convert coordinates from neuropsydia (-10:10) to pygame's system (in pixels).

        Parameters
        ----------
        x = float
            [-10:10]
        y = float
            [-10:10]
        distance_x = convert a horizontal distance
            [-10:10]
        distance_y = convert a horizontal distance
            [-10:10]
        Returns
        ----------
        NA

        Example
        ----------
        NA

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - pygame 1.9.2
        """
        if x != None and y == None:
            x = (x+10.0)/(10.0+10.0)*(screen_width-0.0)+0.0
            return(int(x))
        if x == None and y != None:
            y = (-y+10.0)/(10.0+10.0)*(screen_height-0.0)+0.0
            return(int(y))
        if x != None and y != None:
            x = (x+10.0)/(10.0+10.0)*(screen_width-0.0)+0.0
            y = (-y+10.0)/(10.0+10.0)*(screen_height-0.0)+0.0
            return(int(x),int(y))
        if distance_x != None:
            distance_x = (distance_x)/(10.0+10.0)*(screen_width-0.0)+0.0
            return(int(distance_x))
        if distance_y != None:
            distance_y = (-distance_y)/(10.0+10.0)*(screen_height-0.0)+0.0
            return(int(distance_y))
    def from_pygame(x=None,y=None):
        """
        Help incomplete, sorry.

        Parameters
        ----------
        NA

        Returns
        ----------
        NA

        Example
        ----------
        NA

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - pygame 1.9.2
        """
        if x != None and y == None:
            x =20*x/screen_width - 10
            return(x)
        if x == None and y != None:
            y = -(20*y/screen_height) + 10
            return(y)
        if x != None and y != None:
            x =20*x/screen_width - 10
            y = -(20*y/screen_height) + 10
            return(x,y)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
class Font_Cache_Init:
    def __init__(self):
        self.cache = {}  #Initialize an empty cache
    def get(self,font_path,size):
        if not (font_path,int(size)) in self.cache:  #if not in cache,
            if os.path.exists(font_path):  #if the path leads to a font,
                self.cache[font_path,int(size)] = pygame.font.Font(font_path, int(size))  #load this font
            else:
                self.cache[font_path,int(size)] = pygame.font.SysFont(font_path, int(size))  #load a system font
        return(self.cache[font_path,int(size)])
global Font
Font = Font_Cache_Init()  #Create the font object that will update itself with the different loaded fonts

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
color_list = {
"white":(255,255,255),
"w":(255,255,255),
"black":(0,0,0),
"b":(0,0,0),
"grey":(128,128,128),
"lightgrey":(220,220,220),
"darkgrey":(105,105,105),
"raw_green":(0,255,0 ),
"green":(56,142,60),
"raw_red":(255,0,0),
"red":(213,0,0),
"raw_blue":(0, 0, 255),
"blue":(25,118,210),
"yellow":(255,255,51),
"amber":(255,171,0),
"pink":(255,0,255),

"pale_pink":(255,128,171),
"pale_purple":(234,128,252),
"pale_deep_purple":(179,136,255),
"pale_indigo":(140,158,255),
"pale_blue":(130,177,255),
"pale_light_blue":(128,216,255),
"pale_cyan":(132,255,255),
"pale_teal":(167,255,235),

"violet":(127,0,255),
"lightblue":(0,106,255),
"orange":(255,165,0),
"blue_shade":[(204,229,255),(153,204,255),(102,178,222),(51,153,255),(0,128,255)],
"red_shade":[(255,204,204),(255,153,153),(255,102,102),(255,51,51),(255,0,0)],
"green_shade":[(204,255,204),(153,255,153),(102,255,102),(51,255,51),(0,255,0)],
"multi_shade":[(255,51,51),(255,51,255),(51,153,255),(51,255,51),(255,153,51)]
}

def color(color):
    """
    Returns an RGB color tuple (or list) from its name.

    Parameters
    ----------
    color = str
        one from the color_list list

    Returns
    ----------
    tuple or list

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> print(n.color_list)
    >>> print(n.color("blue"))
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    None
    """
    if isinstance(color,str):
        try:
            return(color_list[color])
        except:
            print("NEUROPSYDIA WARNING: color() was used, however the argument " + str(color) + " was not detected and might cause errors.")
            return(color)
    else:
        return(color)

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def cursor(visible=True):
    """
    Set the mouse cursor to visible or invisible.

    Parameters
    ----------
    visible = bool
        True for visible, False for invisible.

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.cursor(True)
    >>> n.time.wait(2000)
    >>> n.close()

    Authors
    ----------
    The pygame team

    Dependencies
    ----------
    - pygame 1.9.2
    """
    pygame.mouse.set_visible(visible)