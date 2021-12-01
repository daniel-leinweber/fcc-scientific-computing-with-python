import copy
import random

class Hat:
  def __init__(self, **args):
    self.contents = [key for key, value in args.items() for _ in range(value)]

  def draw(self, number_of_balls):
    number_of_balls = min(number_of_balls, len(self.contents))
    return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(number_of_balls)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  times_hit = 0
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    balls_req = sum([1 for key, value in expected_balls.items() if balls_drawn.count(key) >= value])
    times_hit += 1 if balls_req == len(expected_balls) else 0
  
  return times_hit / num_experiments
