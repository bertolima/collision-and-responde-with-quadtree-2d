from Screen import Screen

# pygame setup
screen = Screen(800,800)

#gameloop
while screen.isRunning():
    screen.update()
    screen.render()
screen.stop()