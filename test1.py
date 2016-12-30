import pygame


class DrawLine:
    def __init__(self, display_surface):
        self.running = True
        self.display_surface = display_surface
        self.size = self.weight, self.height = 640, 400
        self.fps = 60
        self.clock = pygame.time.Clock()

    def draw(self, surface):
        pygame.draw.line(surface, color, self.start_pos, self.end_pos, width=5)

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_execute(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.flip()
            self.clock.tick(self.fps)
        self.on_cleanup()
