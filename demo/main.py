from adcsim.actuator import PFDA
from adcsim.spacecraft import Spacecraft

b9 = Spacecraft(actuators=[PFDA(gain=80e-6, time_constant=0.5)])
