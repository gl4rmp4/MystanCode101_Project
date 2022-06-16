"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 500  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball
COLOR_LIST = ['red', 'orange', 'yellow', 'green', 'blue']


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.paddle_offset = PADDLE_OFFSET
        self.ball_radius = ball_radius

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=(self.window.height - self.paddle_offset - self.paddle.height))
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) // 2,
                        y=(self.window.height - self.ball.height) // 2)
        # Create brick
        color_counter = -1 #給予color list 計算起始值
        for i in range(BRICK_ROWS):
            if i % 2 == 0:
                color_counter += 1
            for j in range(BRICK_COLS):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.window.add(self.brick, x=((brick_width + BRICK_SPACING) * j),
                                y=((brick_height + BRICK_SPACING) * (i + 2)))
                self.brick.fill_color = COLOR_LIST[color_counter] # color list

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        onmouseclicked(self.start)
        onmousemoved(self.follow)
        self.is_click = False  # Already click gate
        self.click_gate = False  # Click gate
        self.num_finish = BRICK_COLS * BRICK_ROWS

    def start(self, ball_event):
        if not self.is_click:  # After click random not turn on by click
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.is_click = True
        self.click_gate = True  # start click

    def follow(self, paddle_follow):
        if (self.paddle.width / 2) <= paddle_follow.x <= self.window.width - (self.paddle.width / 2):
            self.window.add(self.paddle, x=paddle_follow.x - self.paddle.width / 2, y=self.paddle.y)

    # getter
    # Define getter velocity_x
    def get_ball_velocity_x(self):
        return self.__dx

    # Define getter velocity_y
    def get_ball_velocity_y(self):
        return self.__dy

    # setter
    # Define setter velocity_x
    def set_ball_velocity_direction_x(self):
        self.__dx = -self.__dx
        return self.__dx

    # Define setter velocity_y
    def set_ball_velocity_direction_y(self):
        self.__dy = -self.__dy
        return self.__dy

    # Define getter ball_radius
    def get_ball_radius(self):
        return self.ball_radius

    def set_click_gate(self):
        self.click_gate = False
        return self.click_gate

    # Define the game boundary
    def game_bounce(self):
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball_radius * 2:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    # Define the ball meet the brick or paddle
    def meet_the_object(self):
        # if self.ball.y < self.window.height * 0.5:
        for corner_x in range(self.ball.x, self.ball.x + self.ball.width + 1, self.ball.width):
            for corner_y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                object_detected = self.window.get_object_at(corner_x, corner_y)
                if object_detected:
                    if object_detected is not self.paddle:
                        self.window.remove(object_detected)
                        self.num_finish -= 1
                        self.__dy *= -1
                        return
                    elif object_detected is self.paddle:
                        if self.__dy > 0:
                            self.__dy *= -1
                        return

        # #  ball up side boundary 此寫法會發生偵測邊 共同撞到一個方塊 無法分辨只消一次還是兩次
        # if self.window.get_object_at(self.ball.x, self.ball.y) is not None and \
        #         self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y) is not None:
        #     self.__dy = -self.__dy
        #     self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
        #     self.window.remove(self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y))
        #     self.num_finish -= 2
        # # ball bottom side boundary
        # elif self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS) is not None and \
        #         self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS) is not None:
        #     self.__dy = -self.__dy
        #     self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS))
        #     self.window.remove(
        #         self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS))
        #     self.num_finish -= 2
        # # ball left side boundary
        # elif self.window.get_object_at(self.ball.x, self.ball.y) is not None and \
        #         self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS) is not None:
        #     self.__dx = -self.__dx
        #     self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
        #     self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS))
        #     self.num_finish -= 2
        #
        # # ball right side boundary
        # elif self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y) is not None and \
        #         self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS) is not None:
        #     self.__dx = -self.__dx
        #     self.window.remove(self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y))
        #     self.window.remove(
        #         self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS))
        #     self.num_finish -= 2
        # elif self.window.get_object_at(self.ball.x, self.ball.y) is not None:
        #     self.__dx = -self.__dx
        #     self.__dy = -self.__dy
        #     self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))  # point 1
        #     self.num_finish -= 1
        # elif self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y) is not None:
        #     self.__dx = -self.__dx
        #     self.__dy = -self.__dy
        #     self.window.remove(self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y))  # point 2
        #     self.num_finish -= 1
        # elif self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS,
        #                              self.ball.y + 2 * BALL_RADIUS) is not None:
        #     self.__dx = -self.__dx
        #     self.__dy = -self.__dy
        #     self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS))  # point 3
        #     self.num_finish -= 1
        # elif self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS) is not None:
        #     self.__dx = -self.__dx
        #     self.__dy = -self.__dy
        #     self.window.remove(
        #         self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS,
        #                                   self.ball.y + 2 * BALL_RADIUS))  # point 4
        #     self.num_finish -= 1

    #
    # else:
    #     if self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS,
    #                                  self.ball.y + 2 * BALL_RADIUS) is not None and \
    #             self.ball.y + 2 * BALL_RADIUS >= self.paddle.y or self.window.get_object_at(self.ball.x,
    #                                                                                         self.ball.y + 2 * BALL_RADIUS) is not None and self.ball.y + 2 * BALL_RADIUS >= self.paddle.y:
    #         if self.__dy > 0:
    #             self.__dy = -self.__dy
    #     if self.window.get_object_at(self.ball.x,
    #                                  self.ball.y) is not None and \
    #             self.paddle.y + self.paddle.width > self.ball.y + 2 * BALL_RADIUS > self.paddle.y or \
    #             self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS) is not None and \
    #             self.paddle.y + self.paddle.width > self.ball.y + 2 * BALL_RADIUS > self.paddle.y:
    #         self.__dx = -self.__dx
    #         print(5)
    #     if self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS,
    #                                  self.ball.y) is not None and \
    #             self.paddle.y + self.paddle.width > self.ball.y + 2 * BALL_RADIUS > self.paddle.y or \
    #             self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS) is not None \
    #             and self.paddle.y + self.paddle.width > self.ball.y + 2 * BALL_RADIUS > self.paddle.y:
    #         self.__dx = -self.__dx
    #         print(9)

    def restart(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width) // 2,
                        y=(self.window.height - self.ball.height) // 2)
