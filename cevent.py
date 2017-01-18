from pygame.locals import *


class CEvent:
    def __init__(self):
        pass

    def on_input_focus(self):
        pass

    def on_input_blur(self):
        pass

    def on_key_down(self, event):
        pass

    def on_key_up(self, event):
        pass

    def on_mouse_focus(self):
        pass

    def on_mouse_blur(self):
        pass

    def on_mouse_move(self, event):
        pass

    def on_mouse_wheel(self, event):
        pass

    def on_lmb_up(self, event):
        pass

    def on_lmb_down(self, event):
        pass

    def on_rmb_up(self, event):
        pass

    def on_rmb_down(self, event):
        pass

    def on_mmb_up(self, event):
        pass

    def on_mmb_down(self, event):
        pass

    def on_minimize(self):
        pass

    def on_restore(self):
        pass

    def on_resize(self, event):
        pass

    def on_expose(self):
        pass

    def on_exit(self):
        pass

    def on_user(self, event):
        pass

    def on_joy_axis(self, event):
        pass

    def on_joybutton_up(self, event):
        pass

    def on_joybutton_down(self, event):
        pass

    def on_joy_hat(self, event):
        pass

    def on_joy_ball(self, event):
        pass

    def on_event(self, event):
        if event.type == QUIT:
            self.on_exit()

        elif event.type >= USEREVENT:
            self.on_user(event)

        elif event.type == VIDEOEXPOSE:
            self.on_expose()

        elif event.type == VIDEORESIZE:
            self.on_resize(event)

        elif event.type == KEYUP:
            self.on_key_up(event)

        elif event.type == KEYDOWN:
            self.on_key_down(event)

        elif event.type == MOUSEMOTION:
            self.on_mouse_move(event)

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.on_lmb_down(event)
            elif event.button == 2:
                self.on_mmb_down(event)
            elif event.button == 3:
                self.on_rmb_down(event)

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.on_lmb_up(event)
            elif event.button == 2:
                self.on_mmb_up(event)
            elif event.button == 3:
                self.on_rmb_up(event)

        elif event.type == ACTIVEEVENT:
            if event.state == 1:
                if event.gain:
                    self.on_mouse_focus()
                else:
                    self.on_mouse_blur()
            elif event.state == 2:
                if event.gain:
                    self.on_input_focus()
                else:
                    self.on_input_blur()
            elif event.state == 4:
                if event.gain:
                    self.on_restore()
                else:
                    self.on_minimize()


if __name__ == "__main__":
    event = CEvent()
