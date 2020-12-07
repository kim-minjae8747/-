from time import sleep
import tellopy

def handler(event,sender,data,**args):
    drone = sender
    if even is drone.EVENT_FLIGHT_DATA:
        print(data)

def test():
    drone = tellopy.Tello()
    try:
        drone.subcribe(drone.EVENT_FLIGHT_DATA,handler)
        drone.connect()
        drone.wait_for_connection(60,0)
        drone.takeoff()
        sleep(5)
        drone.forward(20)
        sleep(5)
        drone.forward(25)
        drone.clockwise(25)
        drone.forward(10)
        sleep(3)
        drone.forward(20)
        drone.counter_clockwise(40)
        drone.forward(30)
        sleep(2)
        drone.forward(10)
        drone.clockwise(40)
        drone.forward(20)
        sleep(3)
        drone.clockwise(25)
        drone.forward(20)
        drone.flip_back()
        drone.forward(40)
        drone.land()
        sleep(5)
 except Exception as ex():
     print(ex)
 finally:
     drone.quit()

if__nabe__=='__main__':
   test()