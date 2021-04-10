import numpy as np


class AngularRate:
    def __init__(self, rate=(0.0, 0.0, 0.0)):
        self.rate = rate
        print(self._rate)

    @classmethod
    def from_degrees(cls, rate):
        """Initialize from angular rate vector in degree per second.
        """
        return cls(np.radians(np.array(rate)))

    def __str__(self):
        """An informal, nicely printable string representation of the AngularRate object.
        """
        return "{:.3f} {:.3f} {:.3f}".format(self._rate[0], self._rate[1], self._rate[2])

    def __repr__(self):
        """The 'official' string representation of the AngularRate object.

        This is a string representation of a valid Python expression that could be
        used to recreate an object with the same value (given an appropriate
        environment)
        """
        return "AngularRate({!r}, {!r}, {!r})".format(self._rate[0], self._rate[1], self._rate[2])

    def derivative(self, inertia=np.eye(3), torques=np.array((0.0, 0.0, 0.0)),angular_momenta=np.array((0.0, 0.0, 0.0))):
        return np.linalg.inv(inertia) @ (torques - np.cross(self._rate, inertia @ self._rate + angular_momenta))

    def update(self, inertia=np.eye(3), torques=np.array((0.0, 0.0, 0.0)), angular_momenta=np.array((0.0, 0.0, 0.0))):
        # TODO: implement update, maybe based on ivp_solve?
        # NOTE: How to deal with parallel updates for actuators and stuff?
        raise NotImplementedError()

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, new):
        self._rate = np.array(new)
