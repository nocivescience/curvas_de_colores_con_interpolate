from manim import *
import itertools as it
class PartialScene(Scene):
  CONFIG={
    'colors':[RED,BLUE,YELLOW],
  }
  def construct(self):
    circles=VGroup()
    colors=it.cycle(self.CONFIG['colors'])
    def update_curve(mob,dt):
        mob.total_time+=dt
        diameter=np.linalg.norm(
            mob.template.point_from_proportion(0)-
            mob.template.point_from_proportion(.6)
        )
        modulus=np.sqrt(diameter)+.1
        alpha=(mob.total_time%modulus)/modulus
        mob.pointwise_become_partial(
            circle.template,
            max(interpolate(-1,1,alpha),0),
            min(interpolate(0,2,alpha),1)
        )
    for _ in range(200):
        circle=Circle(radius=4*np.random.random(),stroke_width=12).set_color(next(colors))
        circle.total_time=0
        circle.template=circle.copy()
        circle.add_updater(update_curve)
        circles.add(circle)
        self.add(circles)
    self.wait(6)