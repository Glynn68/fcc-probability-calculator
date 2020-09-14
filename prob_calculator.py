import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents_dict = kwargs
    self.contents = []
    # create contents list
    for colour, amount in self.contents_dict.items():
      for i in range (amount):
        self.contents.append(colour)
    
  
  def draw(self, num_balls):
    drawn_bag = []
    for i in range(num_balls):
      j = random.randint(0,len(self.contents)-1)
      drawn_bag.append(self.contents.pop(j))
      if len(self.contents) == 0:
        return drawn_bag
    return drawn_bag



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  cum_draw = {}
  for x in expected_balls:
    cum_draw[x]=0
  m = 0

  for n in range (num_experiments):
    cum_draw = {}
    draw_count = 0
    for x in expected_balls:
      cum_draw[x]=0
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw (num_balls_drawn)
    for x in expected_balls:
      for i in drawn:
        if i == x:
          cum_draw[x] += 1
      if cum_draw[x] >= expected_balls[x]:
        draw_count += 1
    if draw_count == len(expected_balls):
      m += 1
  return m/num_experiments
          
    
  

