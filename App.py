import pygame
import random

import test1
import cevent


class App(cevent.CEvent):
    def __init__(self):
        self.running = True
        self.display_surface = None
        self.size = self.weight, self.height = 640, 400
        self.fps = 60
        self.clock = pygame.time.Clock()
        pygame.init()
        self.display_surface = pygame.display.set_mode(self.size,
                                                       pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.running = True
        self.grid = test1.Grid(self.display_surface, (255, 0, 0), (0, 255, 0), 0, 0, 8, 8,
                               self.display_surface.get_size()[0],
                               self.display_surface.get_size()[1], 5)

    def on_loop(self):
        pass

    def on_render(self):
        self.display_surface.fill((255, 255, 255))
        pygame.display.flip()

    def on_exit(self):
        self.running = False

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.clock.tick(self.fps)
        self.on_cleanup()

    def on_event2(self, event):
        # print(pygame.event.event_name(event.type))
        if event.type == pygame.QUIT:
            print('User asked to quit.')
            self.running = False
        elif event.type == pygame.KEYDOWN:
            print('User pressed a key.')
            if event.key == pygame.K_SPACE:
                print('space pressed')
        elif event.type == pygame.KEYUP:
            print('User let go of a key.')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cell = self.grid.cell_by_pos(pygame.mouse.get_pos())
            if cell:
                print('Clicked cell: ' + str(cell.id))
                print('Clicked cell: ' + str(cell.color))
                cell.color = (
                    random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                print('Clicked cell: ' + str(cell.color))
        # elif event.type == pygame.MOUSEMOTION:
        # elif event.type == pygame.MOUSEBUTTONUP:
        elif event.type == pygame.VIDEORESIZE:
            self.size = event.dict['size']
            print('Screen resized to:')
            print(self.size)
            self.display_surface = pygame.display.set_mode(self.size,
                                                           pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

    def on_resize(self, event):
        self.size = event.dict['size']
        print('Screen resized to:')
        print(self.size)
        self.display_surface = pygame.display.set_mode(self.size,
                                                       pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)


if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
