from typing import Type
import numpy as np
from pyquaternion import Quaternion
from adcsim.util import AngularRate

class Spacecraft:
    def __init__(self, inertia=np.eye(3), attitude=Quaternion(1), angular_rate=AngularRate(), disturbances=[None], actuators=[None], controller=None):
        self.angular_rate = angular_rate
        self.attitude = attitude
        self.disturbances = disturbances
        self.inertia = inertia

    # TODO: add actuators property

    @property
    def angular_rate(self):
        return self._angular_rate

    @angular_rate.setter
    def angular_rate(self, new):
        if type(new) is AngularRate:
            self._angular_rate = new
        else:
            raise TypeError('Angular rate must be of type AngularRate')

    @property
    def attitude(self):
        return self._attitude

    @attitude.setter
    def attitude(self, new):
        if type(new) is Quaternion:
            self._attitude = new
        else:
            # TODO: check out, if try Quaternion(new) could be of good use here?
            raise TypeError('Attitude must be of type Quaternion')

    # TODO: add controller property

    @property
    def disturbances(self):
        return self._disturbances

    @disturbances.setter
    def disturbances(self, new):
        if len(self._disturbances) == 0:
            # TODO: this does not handle inputting single disturbances into a list or setting to an input list properly
            self._disturbances = new
        else:
            raise TypeError("Disturbances vector not empty - please use obj.disturbances.append(...)")

    @property
    def inertia(self):
        return self._inertia

    @inertia.setter
    def inertia(self, new):
        # TODO: check if new inertia is a proper inertia tensor
        self._inertia = new