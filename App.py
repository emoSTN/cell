import pygame


class App:
    def __init__(self):
        self.running = True
        self.display_surface = None
        self.size = self.weight, self.height = 640, 400
        self.fps = 60
        self.clock = pygame.time.Clock()
        pygame.init()
        self.display_surface = pygame.display.set_mode(self.size,
                                                       pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.lines = []
        self.start_pos = 0, 0
        self.curr_pos = 0, 0
        self.end_pos = 0, 0
        self.plot = False
        self.draw = False
        self.clean = False

    def on_event(self, event):
        # print(pygame.event.event_name(event.type))
        if event.type == pygame.QUIT:
            print('User asked to quit.')
            self.running = False
        elif event.type == pygame.KEYDOWN:
            print('User pressed a key.')
            if event.key == pygame.K_SPACE:
                print('space pressed')
                self.clean = True
        elif event.type == pygame.KEYUP:
            print('User let go of a key.')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('User pressed a mouse button')
            self.start_pos = pygame.mouse.get_pos()
            self.draw = True
            self.plot = True
        elif event.type == pygame.MOUSEMOTION:
            if self.draw:
                self.plot = True
                self.curr_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.draw:
                self.end_pos = pygame.mouse.get_pos()
                self.plot = False
                self.draw = False
                self.lines.append((self.start_pos, self.end_pos))
        elif event.type == pygame.VIDEORESIZE:
            self.size = event.dict['size']
            print('Screen resized to:')
            print(self.size)
            self.display_surface = pygame.display.set_mode(self.size,
                                                           pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

    def on_loop(self):
        pass

    def on_render(self):
        if self.draw:
            if self.plot:
                self.curr_pos = pygame.mouse.get_pos()
                pygame.draw.line(self.display_surface, (255, 0, 0), self.start_pos, self.curr_pos, 1)
                self.plot = False
            else:
                self.end_pos = pygame.mouse.get_pos()
                pygame.draw.line(self.display_surface, (0, 255, 0), self.start_pos, self.end_pos, 5)
        if self.clean:
            self.lines = []
            self.clean = False
            self.draw = False
            self.plot = False
            self.display_surface.fill((255, 255, 255))
            pygame.display.flip()
        if len(self.lines) > 0:
            for line in self.lines:
                pygame.draw.line(self.display_surface, (0, 255, 0), line[0], line[1], 5)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.display_surface.fill((255, 255, 255))
        pygame.display.flip()
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            if self.draw:
                self.display_surface.fill((255, 255, 255))
            self.on_render()
            pygame.display.flip()
            self.clock.tick(self.fps)
        self.on_cleanup()


if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
