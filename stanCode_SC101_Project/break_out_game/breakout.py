"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 1000 / 180  # 120 frames per second
NUM_LIVES = 3  # Number of attempts
# Global
Lives = NUM_LIVES


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    while True:
        global Lives
        pause(FRAME_RATE)
        graphics.meet_the_object()
        graphics.game_bounce()
        if graphics.click_gate:
            graphics.ball.move(graphics.get_ball_velocity_x(), graphics.get_ball_velocity_y())
        if graphics.ball.y >= graphics.window.height:
            Lives -= 1
            graphics.restart()
            graphics.set_click_gate()
        if Lives == 0 or graphics.num_finish == 0:
            break
    print('End')








if __name__ == '__main__':
    main()
