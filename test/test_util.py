from adcsim.util import AngularRate

import numpy as np
import math

def test_angularRate_rate():
    angular_rate = AngularRate()

    assert type(angular_rate.rate) is np.ndarray
    assert angular_rate.rate[0] == 0
    assert angular_rate.rate[1] == 0
    assert angular_rate.rate[2] == 0

def test_angularRate_intializeFromDegrees():
    angular_rate = AngularRate.from_degrees((180., 0., 0.))

    assert type(angular_rate.rate) is np.ndarray
    assert angular_rate.rate[0] == math.pi
    assert angular_rate.rate[1] == 0
    assert angular_rate.rate[2] == 0
