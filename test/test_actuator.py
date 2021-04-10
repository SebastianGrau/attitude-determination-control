from attr import set_run_validators
from adcsim.actuator import Actuator, PFDA

import pytest

import numpy as np

def test_actuator_alignment():
    actuator = Actuator()
    alignment = actuator.alignment
    assert alignment[0] == 1
    assert alignment[1] == 0
    assert alignment[2] == 0

    actuator.alignment = (0., 0., 1.)
    alignment = actuator.alignment
    assert alignment[0] == 0
    assert alignment[1] == 0
    assert alignment[2] == 1

    assert type(actuator.alignment) is np.ndarray


def test_actuator_input():
    # input is initialized to zero
    actuator = Actuator()
    assert actuator.input == 0

    # set input to one
    actuator.input = 1
    assert actuator.input == 1

def test_actuator_angular_momentum():
    actuator = Actuator()

    assert type(actuator.angular_momentum) is np.ndarray
    assert actuator.angular_momentum[0] == 0
    assert actuator.angular_momentum[1] == 0
    assert actuator.angular_momentum[2] == 0

    actuator.angular_momentum = 1
    assert type(actuator.angular_momentum) is np.ndarray
    assert actuator.angular_momentum[0] == 1 * actuator.alignment[0]
    assert actuator.angular_momentum[1] == 1 * actuator.alignment[1]
    assert actuator.angular_momentum[2] == 1 * actuator.alignment[2]

def test_actuator_input():
    actuator = Actuator()

    assert actuator.input == 0

    actuator.input = 1
    assert actuator.input == 1

def test_actuator_torque():
    actuator = Actuator()

    assert type(actuator.torque) is np.ndarray
    assert actuator.torque[0] == 0
    assert actuator.torque[1] == 0
    assert actuator.torque[2] == 0

    actuator.torque = 1
    assert actuator.torque[0] == 1 * actuator.alignment[0]
    assert actuator.torque[1] == 1 * actuator.alignment[1]
    assert actuator.torque[2] == 1 * actuator.alignment[2]

def test_pfda_gain():
    pfda = PFDA()
    assert pfda.gain == 1

    pytest.raises(ValueError, setattr, pfda, "gain", -1)

def test_pfda_input():
    pfda = PFDA()
    assert pfda.input == 0

    pfda.input = 1
    assert pfda.input == 1

    pytest.raises(ValueError, setattr, pfda, "input", 2)

    pfda.input = -1
    assert pfda.input == -1

    pytest.raises(ValueError, setattr, pfda, "input", -2)

def test_pfda_time_constant():
    pfda = PFDA()
    assert pfda.time_constant == 1

    pytest.raises(ValueError, setattr, pfda, "time_constant", 0)
