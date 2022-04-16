from turtle import *

color('orange', 'yellow')
begin_fill()

while True:
  forward(350)
  left(170)
  right(280)
  if abs(pos()) < 1:
    break

end_fill()
done()