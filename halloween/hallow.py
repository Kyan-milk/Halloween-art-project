import turtle as trtl
import random
wn = trtl.Screen()
gifs=['funny-ghost-gif-halloween','gif,halloween-pumpkin.gif', 'skull-animation_3.gif', 'wbe-halloween-pumpkins.gif']
wn.addshape(gifs)
t=trtl
def make_gif():
  t.shape(random(gifs))
t.onclick(make_gif)
wn.mainloop()