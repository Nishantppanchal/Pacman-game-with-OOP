# Version 2.0.4.2
# Latest updates:
# 2.0.4.2
# fixed playSound for Pyglet 1.4.4 +
# 2.0.4.1
# Added stopSound(), disabled streaming sounds
# 2.0.4
# Added support for blocking input()
# 2.0.3.1:
# Removed set_fps_limit due to it missing from Pyglet.clock 1.4.2
# 2.0.3:
# Added drawPixel(), drawRawPixels(), imageFromData()
# 2.0.2:
# Added drawRect(), drawCircle()
# and close() <- by Peter Toronyi

import pyglet
import math
import inspect

from pyglet.window import mouse

# rendering blend types
BLEND_ALPHA = 0
BLEND_ADDITIVE = 1

# Key symbol constants

# ASCII commands
KEY_BACKSPACE = pyglet.window.key.BACKSPACE
KEY_TAB = pyglet.window.key.TAB
KEY_LINEFEED = pyglet.window.key.LINEFEED
KEY_CLEAR = pyglet.window.key.CLEAR
KEY_RETURN = pyglet.window.key.RETURN
KEY_ENTER = pyglet.window.key.ENTER
KEY_PAUSE = pyglet.window.key.PAUSE
KEY_SCROLLLOCK = pyglet.window.key.SCROLLLOCK
KEY_SYSREQ = pyglet.window.key.SYSREQ
KEY_ESCAPE = pyglet.window.key.ESCAPE
KEY_SPACE = pyglet.window.key.SPACE

# Cursor control and motion
KEY_HOME = pyglet.window.key.HOME
KEY_LEFT = pyglet.window.key.LEFT
KEY_UP = pyglet.window.key.UP
KEY_RIGHT = pyglet.window.key.RIGHT
KEY_DOWN = pyglet.window.key.DOWN
KEY_PAGEUP = pyglet.window.key.PAGEUP
KEY_PAGEDOWN = pyglet.window.key.PAGEDOWN
KEY_END = pyglet.window.key.END
KEY_BEGIN = pyglet.window.key.BEGIN

# Misc functions
KEY_DELETE = 0xffff
KEY_SELECT = 0xff60
KEY_PRINT = 0xff61
KEY_EXECUTE = 0xff62
KEY_INSERT = 0xff63
KEY_UNDO = 0xff65
KEY_REDO = 0xff66
KEY_MENU = 0xff67
KEY_FIND = 0xff68
KEY_CANCEL = 0xff69
KEY_HELP = 0xff6a
KEY_BREAK = 0xff6b
KEY_MODESWITCH = 0xff7e
KEY_SCRIPTSWITCH = 0xff7e
KEY_FUNCTION = 0xffd2

# Text motion constants: these are allowed to clash with key constants
KEY_MOTION_UP = KEY_UP
KEY_MOTION_RIGHT = KEY_RIGHT
KEY_MOTION_DOWN = KEY_DOWN
KEY_MOTION_LEFT = KEY_LEFT
KEY_MOTION_NEXT_WORD = 1
KEY_MOTION_PREVIOUS_WORD = 2
KEY_MOTION_BEGINNING_OF_LINE = 3
KEY_MOTION_END_OF_LINE = 4
KEY_MOTION_NEXT_PAGE = KEY_PAGEDOWN
KEY_MOTION_PREVIOUS_PAGE = KEY_PAGEUP
KEY_MOTION_BEGINNING_OF_FILE = 5
KEY_MOTION_END_OF_FILE = 6
KEY_MOTION_BACKSPACE = KEY_BACKSPACE
KEY_MOTION_DELETE = KEY_DELETE

# Number pad
KEY_NUMLOCK = 0xff7f
KEY_NUM_SPACE = 0xff80
KEY_NUM_TAB = 0xff89
KEY_NUM_ENTER = 0xff8d
KEY_NUM_F1 = 0xff91
KEY_NUM_F2 = 0xff92
KEY_NUM_F3 = 0xff93
KEY_NUM_F4 = 0xff94
KEY_NUM_HOME = 0xff95
KEY_NUM_LEFT = 0xff96
KEY_NUM_UP = 0xff97
KEY_NUM_RIGHT = 0xff98
KEY_NUM_DOWN = 0xff99
KEY_NUM_PRIOR = 0xff9a
KEY_NUM_PAGE_UP = 0xff9a
KEY_NUM_NEXT = 0xff9b
KEY_NUM_PAGE_DOWN = 0xff9b
KEY_NUM_END = 0xff9c
KEY_NUM_BEGIN = 0xff9d
KEY_NUM_INSERT = 0xff9e
KEY_NUM_DELETE = 0xff9f
KEY_NUM_EQUAL = 0xffbd
KEY_NUM_MULTIPLY = 0xffaa
KEY_NUM_ADD = 0xffab
KEY_NUM_SEPARATOR = 0xffac
KEY_NUM_SUBTRACT = 0xffad
KEY_NUM_DECIMAL = 0xffae
KEY_NUM_DIVIDE = 0xffaf

KEY_NUM_0 = 0xffb0
KEY_NUM_1 = 0xffb1
KEY_NUM_2 = 0xffb2
KEY_NUM_3 = 0xffb3
KEY_NUM_4 = 0xffb4
KEY_NUM_5 = 0xffb5
KEY_NUM_6 = 0xffb6
KEY_NUM_7 = 0xffb7
KEY_NUM_8 = 0xffb8
KEY_NUM_9 = 0xffb9

# Function keys
KEY_F1 = 0xffbe
KEY_F2 = 0xffbf
KEY_F3 = 0xffc0
KEY_F4 = 0xffc1
KEY_F5 = 0xffc2
KEY_F6 = 0xffc3
KEY_F7 = 0xffc4
KEY_F8 = 0xffc5
KEY_F9 = 0xffc6
KEY_F10 = 0xffc7
KEY_F11 = 0xffc8
KEY_F12 = 0xffc9
KEY_F13 = 0xffca
KEY_F14 = 0xffcb
KEY_F15 = 0xffcc
KEY_F16 = 0xffcd
KEY_F17 = 0xffce
KEY_F18 = 0xffcf
KEY_F19 = 0xffd0
KEY_F20 = 0xffd1

# Modifiers
KEY_LSHIFT = 0xffe1
KEY_RSHIFT = 0xffe2
KEY_LCTRL = 0xffe3
KEY_RCTRL = 0xffe4
KEY_CAPSLOCK = 0xffe5
KEY_LMETA = 0xffe7
KEY_RMETA = 0xffe8
KEY_LALT = 0xffe9
KEY_RALT = 0xffea
KEY_LWINDOWS = 0xffeb
KEY_RWINDOWS = 0xffec
KEY_LCOMMAND = 0xffed
KEY_RCOMMAND = 0xffee
KEY_LOPTION = 0xffef
KEY_ROPTION = 0xfff0

# Latin-1
KEY_SPACE = 0x020
KEY_EXCLAMATION = 0x021
KEY_DOUBLEQUOTE = 0x022
KEY_HASH = 0x023
KEY_POUND = 0x023  # synonym
KEY_DOLLAR = 0x024
KEY_PERCENT = 0x025
KEY_AMPERSAND = 0x026
KEY_APOSTROPHE = 0x027
KEY_PARENLEFT = 0x028
KEY_PARENRIGHT = 0x029
KEY_ASTERISK = 0x02a
KEY_PLUS = 0x02b
KEY_COMMA = 0x02c
KEY_MINUS = 0x02d
KEY_PERIOD = 0x02e
KEY_SLASH = 0x02f
KEY__0 = 0x030
KEY__1 = 0x031
KEY__2 = 0x032
KEY__3 = 0x033
KEY__4 = 0x034
KEY__5 = 0x035
KEY__6 = 0x036
KEY__7 = 0x037
KEY__8 = 0x038
KEY__9 = 0x039
KEY_COLON = 0x03a
KEY_SEMICOLON = 0x03b
KEY_LESS = 0x03c
KEY_EQUAL = 0x03d
KEY_GREATER = 0x03e
KEY_QUESTION = 0x03f
KEY_AT = 0x040
KEY_BRACKETLEFT = 0x05b
KEY_BACKSLASH = 0x05c
KEY_BRACKETRIGHT = 0x05d
KEY_ASCIICIRCUM = 0x05e
KEY_UNDERSCORE = 0x05f
KEY_GRAVE = 0x060
KEY_QUOTELEFT = 0x060
KEY_A = 0x061
KEY_B = 0x062
KEY_C = 0x063
KEY_D = 0x064
KEY_E = 0x065
KEY_F = 0x066
KEY_G = 0x067
KEY_H = 0x068
KEY_I = 0x069
KEY_J = 0x06a
KEY_K = 0x06b
KEY_L = 0x06c
KEY_M = 0x06d
KEY_N = 0x06e
KEY_O = 0x06f
KEY_P = 0x070
KEY_Q = 0x071
KEY_R = 0x072
KEY_S = 0x073
KEY_T = 0x074
KEY_U = 0x075
KEY_V = 0x076
KEY_W = 0x077
KEY_X = 0x078
KEY_Y = 0x079
KEY_Z = 0x07a
KEY_BRACELEFT = 0x07b
KEY_BAR = 0x07c
KEY_BRACERIGHT = 0x07d
KEY_ASCIITILDE = 0x07e

MOUSE_BUTTON_NONE = 0
MOUSE_BUTTON_LEFT = 1
MOUSE_BUTTON_RIGHT = 2
MOUSE_BUTTON_MIDDLE = 3

from pyglet.gl import *


class JMSSPygletApp(pyglet.window.Window):
    def __init__(self, fps, graphics, *args, **kwargs):
        super(JMSSPygletApp, self).__init__(width=graphics.width,
                                            height=graphics.height, caption=graphics.title,
                                            fullscreen=graphics.fullscreen,
                                            vsync=True,
                                            *args,
                                            **kwargs)

        self.keys = dict([(a, False) for a in range(255)] +
                         [(a, False) for a in range(0xff00, 0xffff)])

        self.graphics = graphics
        self.draw_func = None
        self.init_func = None

        pyglet.gl.glClearColor(0.5, 0, 0, 1)
        self.fps = fps

        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_dx = 0
        self.mouse_dy = 0

        self.mouse_button_pressed = MOUSE_BUTTON_NONE
        self.mouse_button_released = MOUSE_BUTTON_NONE

        self.renderType = 0  # 1 = sprite, 2 = label, 3 = vertices
        self.blend_type = BLEND_ALPHA
        self.texture = None

        self.closed = False

        self.keyboard_buffer = []
        self.keyboard_buffer_len = 50

        self.last_key = None

        # self.set_mouse_visible(False)

    def start(self):
        if (self.init_func is not None):
            self.init_func()
        pyglet.clock.schedule_interval(self.mainloop, 1.0 / self.fps)
        # removing for compatibility with Pyglet 1.4.2
        # pyglet.clock.set_fps_limit(self.fps)

    def reveal(self):
        if self.closed:
            return False

        pyglet.clock.tick()

        self.switch_to()
        self.dispatch_events()
        # self.dispatch_event('on_draw')

        if self.closed:
            return False

        glEnable(GL_BLEND)

        if self.blend_type == BLEND_ALPHA:
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        elif self.blend_type == BLEND_ADDITIVE:
            glBlendFunc(GL_ONE, GL_ONE)

        for command in self.graphics.commands:
            command[0](**command[1])

        self.graphics._renderPrimitives(self.renderType)

        glDisable(GL_BLEND)

        self.flip()

        # prepare for next frame
        self.invalid = False

        self.renderType = 0
        self.texture = None
        self.vertex_array = []

        self.last_key = None

        return True

    def mainloop(self, dt, *args, **kwargs):
        self.renderType = 0

        self.texture = None

        self.vertex_array = []

        glEnable(GL_BLEND)

        if self.blend_type == BLEND_ALPHA:
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        elif self.blend_type == BLEND_ADDITIVE:
            glBlendFunc(GL_ONE, GL_ONE)

        if (self.draw_func is not None):
            if (len(inspect.signature(self.draw_func)._parameters)) > 0:
                self.draw_func(dt)
            else:
                self.draw_func()

        for command in self.graphics.commands:
            command[0](**command[1])

        self.graphics._renderPrimitives(self.renderType)

        glDisable(GL_BLEND)

        self.graphics.commands = []

        self.invalid = False

    def on_close(self):
        self.closed = True
        self.close()

    def flush_buffer(self):
        self.keyboard_buffer = []

    def get_key_pressed(self):
        return self.last_key

    def on_key_press(self, symbol, modifiers):
        self.last_key = symbol
        self.keys[symbol] = True
        if len(self.keyboard_buffer) > self.keyboard_buffer_len:
            del self.keyboard_buffer[0]
        self.keyboard_buffer.append(symbol)

    def on_key_release(self, symbol, modifiers):
        self.last_key = None
        self.keys[symbol] = False

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.mouse_x = x
        self.mouse_y = y
        self.mouse_dx = dx
        self.mouse_dy = dy
        self.invalid = False

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y
        self.mouse_dx = dx
        self.mouse_dy = dy
        self.invalid = False

    # TODO: implement multiple mouse button press and release in a list
    # currently only 1 button's state is stored at a time
    def on_mouse_press(self, x, y, button, modifiers):
        self.mouse_x = x
        self.mouse_y = y

        if button == pyglet.window.mouse.LEFT:
            self.mouse_button_pressed = MOUSE_BUTTON_LEFT
            self.mouse_button_released = MOUSE_BUTTON_NONE
        elif button == pyglet.window.mouse.MIDDLE:
            self.mouse_button_pressed = MOUSE_BUTTON_MIDDLE
            self.mouse_button_released = MOUSE_BUTTON_NONE
        elif button == pyglet.window.mouse.RIGHT:
            self.mouse_button_pressed = MOUSE_BUTTON_RIGHT
            self.mouse_button_released = MOUSE_BUTTON_NONE

    def on_mouse_release(self, x, y, button, modifiers):
        self.mouse_x = x
        self.mouse_y = y
        if button == pyglet.window.mouse.LEFT:
            self.mouse_button_released = MOUSE_BUTTON_LEFT
            self.mouse_button_pressed = MOUSE_BUTTON_NONE
        elif button == pyglet.window.mouse.MIDDLE:
            self.mouse_button_released = MOUSE_BUTTON_MIDDLE
            self.mouse_button_pressed = MOUSE_BUTTON_NONE
        elif button == pyglet.window.mouse.RIGHT:
            self.mouse_button_released = MOUSE_BUTTON_RIGHT
            self.mouse_button_pressed = MOUSE_BUTTON_NONE


class Graphics:
    def __init__(self, width, height, title="", fps=60, fullscreen=False):
        self.width = width
        self.height = height
        self.title = title
        self.done = False
        self.fps = fps

        self.listeners = []

        self.draw_func = None
        self.update_func = None

        self.soundPlayers = {}
        self.sounds = {}

        self.fullscreen = fullscreen

        self.app = JMSSPygletApp(fps, self)

        self.commands = []

    # returns True if rectangle (x1, y1, x1 + w1, y1 + h1) intersects
    #                 rectangle (x2, y2, x2 + w2, y2 + h2)
    def intersects(self, x1, y1, w1, h1, x2, y2, w2, h2):
        return not( ((x1 + w1) < x2) or \
                    ((x2 + w2) < x1) or \
                    ((y1 + h1) < y2) or \
                    ((y2 + h2) < y1) )

    # returns True if point (px, py) is inside
    #                 rectangle (rx, ry, rx + w, ry + h)
    def isInside(self, rx, ry, w, h, px, py):
        return px >= rx and px <= (rx + w) and py >= ry and py <= (ry + h)


    def run(self):
        self.app.start()
        pyglet.app.run()

    def close(self):
        self.app.close()

    def exit(self):
        pyglet.app.exit()

    def init(self, func):
        self.app.init_func = func

    def refresh(self):
        result = self.app.reveal()

        self.commands = []
        return result

    # alias for reveal()
    def reveal(self):
        return self.refresh()

    def input(self, text, x = 0, y = 0):
        done = False
        self.drawText(text, 100, 100)
        input_string = ""
        self.app.flush_buffer()
        while not done:
            if len(self.app.keyboard_buffer) > 0:
                last_key = self.app.keyboard_buffer[-1]
            else:
                last_key = None
            if last_key == KEY_BACKSPACE:

                del self.app.keyboard_buffer[-1]
                if len(self.app.keyboard_buffer) > 0:
                    del self.app.keyboard_buffer[-1]
            elif last_key == KEY_ENTER:
                del self.app.keyboard_buffer[-1]
                done = True

            input_string = "".join([chr(c) for c in self.app.keyboard_buffer])
            self.commands[-1][1]["text"] = text + input_string + "_"
            self.app.reveal()


        self.app.flush_buffer()
        return input_string


    def mainloop(self, func):
        self.app.draw_func = func

    def clear(self, r=0, g=0, b=0, a=1):
        kwargs = {"r": r, "g": g, "b": b, "a": a}
        self.commands.append([self.__clear, kwargs])

    def __clear(self, r=0, g=0, b=0, a=1):
        pyglet.gl.glClearColor(r, g, b, a)
        self.app.clear()

    def setFPS(self, fps):
        self.fps = fps

    def loadImage(self, file):
        return pyglet.image.load(file)

    def isKeyPressed(self, key):
        return self.app.keys[key]

    def isKeyDown(self, key):
        return self.isKeyPressed(key)

    def isMousePressed(self, key):
        return self.app.mouse_button_pressed == key

    def isMouseReleased(self, key):
        return self.app.mouse_button_released == key

    def getMousePos(self):
        return self.app.mouse_x, self.app.mouse_y

    def getMouseDelta(self):
        return self.app.mouse_dx, self.app.mouse_dy

    def _convColor(self, c):
        return (int(c[0] * 255.0), int(c[1] * 255.0), int(c[2] * 255.0), int(c[3] * 255.0))

    def set_blend_type(self, type):
        self.app.blend_type = type

    def get_blend_type(self):
        return self.app.blend_type

    def loadSound(self, filename, streaming=False):
        # TODO: streaming doesn't work properly
        if filename not in self.sounds:
            self.sounds[filename] = pyglet.media.load(filename=filename, streaming=False)
        return self.sounds[filename]
        

    def playSound(self, sound, loop=False):
        if isinstance(sound, str):
            sound = self.loadSound(sound)


        sound.play()
        '''
        player = pyglet.media.Player()
        sg = pyglet.media.SourceGroup()#sound.audio_format, None)
        sg.queue(sound)
        sg.loop = loop
        self.soundPlayers[sound] = player
        player.queue(sg)
        player.play()
        '''

    def pauseSound(self, sound):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].pause()

    def stopSound(self, sound):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].pause()
            self.soundPlayers[sound].next()

    def _renderPrimitives(self, renderType):
        if renderType == 1:
            if (self.app.texture is not None):
                self._drawTexturedQuads(self.app.texture)
        elif renderType == 3:
            self._drawLines()
        elif renderType == 4:
            self._drawTriangles()
        elif renderType == 5:
            self._drawPoints()

        self.app.vertex_array = []

    def _drawLines(self):
        array = (GLfloat * len(self.app.vertex_array))(*self.app.vertex_array)

        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glInterleavedArrays(GL_C4F_N3F_V3F, 0, array)
        glDrawArrays(GL_LINES, 0, len(self.app.vertex_array) // 10)
        glPopClientAttrib()

    def _drawTriangles(self):
        array = (GLfloat * len(self.app.vertex_array))(*self.app.vertex_array)

        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glInterleavedArrays(GL_C4F_N3F_V3F, 0, array)
        glDrawArrays(GL_TRIANGLES, 0, len(self.app.vertex_array) // 10)
        glPopClientAttrib()

    def _drawPoints(self):
        array = (GLfloat * len(self.app.vertex_array))(*self.app.vertex_array)

        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glInterleavedArrays(GL_C4F_N3F_V3F, 0, array)
        glDrawArrays(GL_POINTS, 0, len(self.app.vertex_array) // 10)
        glPopClientAttrib()

    def _drawTexturedQuads(self, image):
        glEnable(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, image.get_texture().id)

        array = (GLfloat * len(self.app.vertex_array))(*self.app.vertex_array)

        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glInterleavedArrays(GL_T2F_C4F_N3F_V3F, 0, array)
        glDrawArrays(GL_QUADS, 0, len(self.app.vertex_array) // 12)
        glPopClientAttrib()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)

    def drawText(self, text, x, y, fontName="Arial", fontSize=10, color=(1, 1, 1, 1), anchorX="left", anchorY="bottom"):
        kwargs = {"text": text, "x": x, "y": y, "fontName": fontName, "fontSize": fontSize, "color": color,
                  "anchorX": anchorX,
                  "anchorY": anchorY}
        self.commands.append([self.__drawText, kwargs])

    # drawText draws immediately without batching
    def __drawText(self, text, x, y, fontName="Arial", fontSize=10, color=(1, 1, 1, 1), anchorX="left",
                   anchorY="bottom"):
        self._renderPrimitives(self.app.renderType)

        label = pyglet.text.Label(text, color=self._convColor(color), font_name=fontName, font_size=fontSize, x=x, y=y, \
                                  anchor_x=anchorX, anchor_y=anchorY)
        label.draw()

    def drawImage(self, image, x, y, width=None, height=None, rotation=0, anchorX=None, anchorY=None, opacity=1.0,
                  r=1.0, g=1.0, b=1.0, rect=None):
        kwargs = {"image": image, "x": x, "y": y, "width": width, "height": height, "rotation": rotation,
                  "anchorX": anchorX,
                  "anchorY": anchorY, "opacity": opacity, "r": r, "g": g, "b": b, "rect": rect}
        self.commands.append([self.__drawImage, kwargs])

    def __drawImage(self, image, x, y, width=None, height=None, rotation=0, anchorX=None, anchorY=None, opacity=1.0,
                    r=1.0, g=1.0, b=1.0, rect=None):
        if (isinstance(image, str)):
            image = self.loadImage(image)
        if self.app.texture != image or self.app.renderType != 1:
            self._renderPrimitives(self.app.renderType)
            self.app.texture = image
            self.app.renderType = 1

        texture = image.get_texture()
        t = texture.tex_coords
        w, h = texture.width, texture.height
        if width is not None:
            w = width
        if height is not None:
            h = height

        points = []
        points.append([x, y])
        points.append([x + w, y])
        points.append([x + w, y + h])
        points.append([x, y + h])

        if (rotation != 0):
            for point in points:
                point[0] -= x
                point[1] -= y
                if (anchorX is not None):
                    point[0] -= anchorX * w
                if (anchorY is not None):
                    point[1] -= anchorY * h

            rotated = []
            for i in range(0, len(points)):
                rotatedPt = [0, 0]
                rotatedPt[0] = points[i][0] * math.cos(rotation) - points[i][1] * math.sin(rotation)
                rotatedPt[1] = points[i][0] * math.sin(rotation) + points[i][1] * math.cos(rotation)
                rotated.append(rotatedPt)

            for point in rotated:
                point[0] += x
                point[1] += y
                if (anchorX is not None):
                    point[0] += anchorX * w
                if (anchorY is not None):
                    point[1] += anchorY * h

            points = rotated

        final_points = []
        final_points += [points[0][0], points[0][1], \
                         points[1][0], points[1][1], \
                         points[2][0], points[2][1], \
                         points[3][0], points[3][1]]

        texs = []
        texs += [t[0], t[1], \
                 t[3], t[4], \
                 t[6], t[7],
                 t[9], t[10]]

        if opacity is None:
            opacity = 1.0
        colors = []
        colors += [r, g, b, opacity, \
                   r, g, b, opacity, \
                   r, g, b, opacity, \
                   r, g, b, opacity]

        for i in range(4):
            self.app.vertex_array += texs[i * 2:(i + 1) * 2]
            self.app.vertex_array += colors[i * 4:(i + 1) * 4]
            self.app.vertex_array += [0, 0, -1]
            self.app.vertex_array += final_points[i * 2:(i + 1) * 2] + [1]

    def drawLine(self, x1, y1, x2, y2, r=1.0, g=1.0, b=1.0, a=1.0, width=1):
        kwargs = {"x1": x1, "y1": y1, "x2": x2, "y2": y2, "r": r, "g": g, "b": b,
                  "a": a, "width": width}
        self.commands.append([self.__drawLine, kwargs])

    # width is not currently supported
    def __drawLine(self, x1, y1, x2, y2, r=1.0, g=1.0, b=1.0, a=1.0, width=1):
        if self.app.renderType != 3:
            self._renderPrimitives(self.app.renderType)
            self.app.renderType = 3

        # GL_C4F_N3F_V3F
        self.app.vertex_array += [r, g, b, a]
        self.app.vertex_array += [0, 0, -1]
        self.app.vertex_array += [x1, y1, 1]
        self.app.vertex_array += [r, g, b, a]
        self.app.vertex_array += [0, 0, -1]
        self.app.vertex_array += [x2, y2, 1]

    def drawRect(self, x1, y1, x2, y2, r=1.0, g=1.0, b=1.0, a=1.0):
        kwargs = {"x1": x1, "y1": y1, "x2": x2, "y2": y2, "r": r, "g": g, "b": b,
                  "a": a}
        self.commands.append([self.__drawRect, kwargs])

    def __drawRect(self, x1, y1, x2, y2, r=1.0, g=1.0, b=1.0, a=1.0):
        if self.app.renderType != 4:
            self._renderPrimitives(self.app.renderType)
            self.app.renderType = 4

        verts = [x1, y1]
        verts += [x1, y2]
        verts += [x2, y2]
        verts += [x1, y1]
        verts += [x2, y2]
        verts += [x2, y1]

        for i in range(len(verts) // 2):
            self.app.vertex_array += [r, g, b, a]
            self.app.vertex_array += [0, 0, -1]
            self.app.vertex_array += [verts[i * 2], verts[(i * 2) + 1], 1]

    def drawCircle(self, x, y, radius, r=1.0, g=1.0, b=1.0, a=1.0):
        kwargs = {"x": x, "y": y, "radius": radius, "r": r, "g": g, "b": b,
                  "a": a}
        self.commands.append([self.__drawCircle, kwargs])

    def __drawCircle(self, x, y, radius, r=1.0, g=1.0, b=1.0, a=1.0):
        if self.app.renderType != 4:
            self._renderPrimitives(self.app.renderType)
            self.app.renderType = 4

        verts = []
        numTris = int(radius * 5)
        for i in range(numTris):
            # centre point
            verts += [x, y]

            # point 1
            angle = math.radians(float(i) / numTris * 360.0)
            c_x = radius * math.cos(angle) + x
            c_y = radius * math.sin(angle) + y
            verts += [c_x, c_y]

            # point next
            angle = math.radians(float(i + 1) / numTris * 360.0)
            c_x = radius * math.cos(angle) + x
            c_y = radius * math.sin(angle) + y
            verts += [c_x, c_y]

        # GL_C4F_N3F_V3F
        for i in range(numTris):
            self.app.vertex_array += [r, g, b, a]
            self.app.vertex_array += [0, 0, -1]
            self.app.vertex_array += [verts[i * 6], verts[(i * 6) + 1], 1]

            self.app.vertex_array += [r, g, b, a]
            self.app.vertex_array += [0, 0, -1]
            self.app.vertex_array += [verts[i * 6 + 2], verts[(i * 6) + 3], 1]

            self.app.vertex_array += [r, g, b, a]
            self.app.vertex_array += [0, 0, -1]
            self.app.vertex_array += [verts[i * 6 + 4], verts[(i * 6) + 5], 1]

    def drawPixel(self, x, y, r=1.0, g=1.0, b=1.0, a=1.0):
        kwargs = {"x": x, "y": y, "r": r, "g": g, "b": b,
                  "a": a}
        self.commands.append([self.__drawPixel, kwargs])

    def __drawPixel(self, x, y, r=1.0, g=1.0, b=1.0, a=1.0):
        if self.app.renderType != 5:
            self._renderPrimitives(self.app.renderType)
            self.app.renderType = 5

        # GL_C4F_N3F_V3F

        self.app.vertex_array += [r, g, b, a]
        self.app.vertex_array += [0, 0, -1]
        self.app.vertex_array += [x, y, 1]

    def imageFromData(self, data, width, height, format="RGBA"):
        _image = pyglet.image.create(width, height)
        _image.set_data(format, width * len(format), data)
        return _image

    def drawRawPixels(self, data, x, y, width, height):
        if self.app.renderType != 5:
            self._renderPrimitives(self.app.renderType)
            self.app.renderType = 5

        verts = []
        num_points = width * height
        for x2 in range(width):
            for y2 in range(height):
                verts += [x + x2, y + y2]

        colours = []
        for x2 in range(width):
            for y2 in range(height):
                # TODO: alpha not yet supported
                colours += [data[(y2 * width + x2) * 3], \
                            data[(y2 * width + x2) * 3 + 1], \
                            data[(y2 * width + x2) * 3 + 2],
                            1.0]

        # GL_C4F_N3F_V3F
        for i in range(num_points):
            self.app.vertex_array += [colours[i * 4], colours[i * 4 + 1], colours[i * 4 + 2], colours[i * 4 + 3]]
            self.app.vertex_array += [0, 0, -1]
            self.app.vertex_array += [verts[i * 2], verts[i * 2 + 1], 1]
