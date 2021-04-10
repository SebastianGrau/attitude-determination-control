import numpy as np

class Actuator:
  """Actuator base class.
  """
  def __init__(self, alignment=(1.0, 0.0, 0.0), angular_momentum=0, input=0, torque=0):
    self.alignment = alignment
    self.angular_momentum = angular_momentum
    self.input = input
    self.torque = torque

  @property
  def alignment(self):
    return self._alignment

  @alignment.setter
  def alignment(self, new):
    self._alignment = np.array(new)

  @property
  def angular_momentum(self):
    return self._angular_momentum * self._alignment

  @angular_momentum.setter
  def angular_momentum(self, new):
    self._angular_momentum = new

  @property
  def input(self):
    return self._input

  @input.setter
  def input(self, new):
    self._input = new

  @property
  def torque(self):
    return self._torque * self._alignment

  @torque.setter
  def torque(self, new):
    self._torque = new


class PFDA(Actuator):
    def __init__(self, alignment=np.array((1.0, 0.0, 0.0)), angular_momentum=0, gain=1, input=0, time_constant=1, torque=0):
        super().__init__(alignment=alignment, angular_momentum=angular_momentum, input=input, torque=torque)

        self.gain = gain
        self.time_constant = time_constant

    @property
    def gain(self):
        return self._gain

    @gain.setter
    def gain(self, new):
        if new > 0:
            self._gain = new
        else:
            raise ValueError('Negative gain')

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, new):
        if new > 1:
            raise ValueError("Input greater than 1")
        elif new < -1:
            raise ValueError("Input less than -1")
        else:
            self._input = new

    @property
    def time_constant(self):
        return self._time_constant

    @time_constant.setter
    def time_constant(self, new):
        if new > 0:
            self._time_constant = new
        else:
            raise ValueError('Negative time constant')
