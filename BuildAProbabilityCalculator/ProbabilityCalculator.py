import copy
import random
from random import sample

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for x, y in kwargs.items():
            [self.contents.append(x) for _ in range(y)]
            
    def draw(self, num_balls):       
        random_balls = []        
        if len(self.contents) <= num_balls:
            random_balls.extend(self.contents)
            self.contents.clear()
            return random_balls
        else:            
            for _ in range(num_balls):
                random_ball = random.choice(self.contents)
                random_balls.append(random_ball)
                self.contents.remove(random_ball)
            return random_balls

    def replace(self, random_balls):
        self.contents.extend(random_balls)
        
    def __str__(self):
        return f'{self.contents}'
    
hat = Hat(black=1, red=3, green=1)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = True
    num_success = 0

    for i in range(num_experiments):
        selected_balls = {}

        copy_hat = copy.deepcopy(hat) # Have to get a deep copy of object. Why??
        random_balls = copy_hat.draw(num_balls_drawn) # Works, why?
        #random_balls = hat.draw(num_balls_drawn)  wrong does't work, why??
        copy_hat.replace(random_balls) # Works, why??
        #hat.replace(random_balls) # Wrong, doesn't work, why??
        for b in random_balls:
            selected_balls[b] = selected_balls.get(b, 0) + 1

        for k, v in expected_balls.items():
            if selected_balls.get(k, 0) < v:
                success = False
                break
        if success == True:
            num_success += 1      
        success = True
    probability = num_success/num_experiments
    return probability   
    
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=4,
                  num_experiments=2000)
print(probability)