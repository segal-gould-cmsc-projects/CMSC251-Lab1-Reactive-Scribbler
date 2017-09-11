## Noah Segal-Gould <ns2349@bard.edu>
## 2017-09-10
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
            safeToContinueList = [x <= 5500 for x in self.scribbler.getObstacle()]
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
            self.scribbler.turnRight(0.5, 0.25)
            if self.scribbler.getObstacle("left") <= 500 and self.scribbler.getObstacle("center") <= 500:
                print("Stopping; It\'s safe to continue.")
                self.scribbler.stop()
                safeToTurn = False
            print("Obstacle Readings:\n\tLeft: %d, %s\n\tCenter: %d, %s" % (robot.getObstacle(0), \
                                                                                             str(safeToContinueList[0]), \
                                                                                             robot.getObstacle(1), \
                                                                                             str(safeToContinueList[1])))
        self.followTheWall()
        
robot = makeRobot("Scribbler", "/dev/tty.Fluke2-094E-Fluke2")
## robot =  makeRobot("SimScribbler", Simulation())

ReactiveScribbler(robot).followTheWall()
