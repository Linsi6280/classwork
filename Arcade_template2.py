
import arcade


WIDTH = 640
HEIGHT = 480


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    y = 30
    for x in range(70, 640, 100):
      arcade.draw_rectangle_filled(x, y, 30, 60, arcade.color.DARK_BROWN)
      arcade.draw_triangle_filled(x, y + 100, x - 40, y + 30, x + 40, y + 30, arcade.color.DARK_GREEN)


    # Draw in here...
    #arcade.draw_circle_filled(100, 100, 25, arcade.color.BLUE)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
