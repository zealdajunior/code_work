
#KEYDOWN,MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN,QUIT,ACTIVEEVENT(),VIDEORESIZE,VIDEOEXPOSE

#pygame events pygame.event.get() pygame.event.wait(waits until something occurs)
# pygame.event.poll(It returns a single event from the queue)
'''MOUSEMOTION events are issued when the mouse is moved over the Pygame window
The events object contains three values
buttons: a tuple of three values representing the state of the mouse buttons
pos: a tuple of two values representing the x and y coordinates of the mouse pointer
rel: a tuple of two values representing the relative movement of the mouse pointer'''