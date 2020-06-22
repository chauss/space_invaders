from moving_object import MovingObject
from edge_insets import EdgeInsets


class Shot(MovingObject):
    def __init__(self, start_pos_x, start_pos_y):
        MovingObject.__init__(self, image_name="shot.png", start_pos_x=start_pos_x, start_pos_y=start_pos_y)
        self.screen_borders = EdgeInsets(top=-2 * self.image.get_height())
