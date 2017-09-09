## Noah Segal-Gould <ns2349@bard.edu>
## 2017-09-09
## CMSC 251
## Reactive Scribbler Lab

from Myro import *

class ReactiveScribbler:
    def __init__(self, scribbler):
        self.scribbler = scribbler
        self.scribbler.setForwardness("fluke-forward")
        self.scribbler.setIRPower(135)
        
    def followTheWall(self):
        safeToContinue = True
        while safeToContinue:
            safeToContinueList = [x <= 6200 for x in self.scribbler.getObstacle()]
            if all(safeToContinueList):
                print("Going Forward; It\'s safe to continue.")
                self.scribbler.motors(0.5, 0.5)
            else:
                print("Stopping; It\'s NOT safe to continue.")
                self.scribbler.stop()
                safeToContinue = False
            print("Obstacle Readings:\n\tLeft: %d, %s\n\tCenter: %d, %s\n\tRight: %d, %s" % (robot.getObstacle(0), \
                                                                                             str(safeToContinueList[0]), \
                                                                                             robot.getObstacle(1), \
                                                                                             str(safeToContinueList[1]), \
                                                                                             robot.getObstacle(2), \
                                                                                             str(safeToContinueList[2])))
        safeToTurn = True
        while safeToTurn:
            print("Turning Right; It\'s not safe to turn.")
            self.scribbler.motors(0.5, -0.5)
            if self.scribbler.getObstacle(0) == 0:
                print("Stopping; It\'s safe to continue.")
                self.scribbler.stop()
                safeToTurn = False
        self.followTheWall()
        
robot = makeRobot("Scribbler", "/dev/tty.Fluke2-094E-Fluke2")
## robot =  makeRobot("SimScribbler", Simulation())

ReactiveScribbler(robot).followTheWall()
