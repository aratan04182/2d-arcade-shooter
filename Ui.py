import pygame

class UI:

    def __init__(self):

        self.font = pygame.font.SysFont(None, 32)
        self.big_font = pygame.font.SysFont(None, 72)

    def draw_hud(self, screen, player, score):

        # HP
        hp_text = self.font.render(
            f"HP: {player.hp}/{player.max_hp}",
            True,
            (255, 255, 255)
        )
        screen.blit(hp_text, (20, 20))

        # LEVEL
        lv_text = self.font.render(
            f"LV: {player.level}",
            True,
            (100, 255, 100)
        )
        screen.blit(lv_text, (20, 60))

        # SCORE
        score_text = self.font.render(
            f"SCORE: {score}",
            True,
            (255, 255, 0)
        )
        screen.blit(score_text, (20, 100))

        # EXP
        exp_text = self.font.render(
            f"EXP: {player.exp}/{player.next_exp}",
            True,
            (100, 200, 255)
        )
        screen.blit(exp_text, (20, 140))

    def draw_game_over(self, screen, width, height):

        text = self.big_font.render(
            "GAME OVER",
            True,
            (255, 50, 50)
        )

        screen.blit(
            text,
            (width // 2 - text.get_width() // 2,
             height // 2)
        )

    def draw_clear(self, screen, width, height):

        text = self.big_font.render(
            "CLEAR!",
            True,
            (50, 255, 50)
        )

        screen.blit(
            text,
            (width // 2 - text.get_width() // 2,
             height // 2)
        )
