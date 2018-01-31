import pydrake
from pydrake.systems.framework import (DiagramBuilder, VectorSystem)
from pydrake.systems.primitives import SignalLogger
from pydrake.systems.analysis import Simulator
import matplotlib.pyplot as plt

# Define the system.
class SimpleContinuousTimeSystem(VectorSystem):
    def __init__(self):
        VectorSystem.__init__(self,
            0,                           # Zero inputs.
            1)                           # One output.
        self._DeclareContinuousState(1)  # One state variable.

    # xdot = -x + x^3
    def _DoCalcVectorTimeDerivatives(self, context, u, x, xdot):
        xdot[:] = -x + x**3

    # y = x
    def _DoCalcVectorOutput(self, context, u, x, y):
        y[:] = x


# Create a simple block diagram containing our system.
builder = DiagramBuilder()
system = builder.AddSystem(SimpleContinuousTimeSystem())
# TODO(russt): add binding then replace the next two lines with
#   logger = LogOutput(system->get_output_port(0), builder)
logger = builder.AddSystem(SignalLogger(1))
builder.Connect(system.get_output_port(0), logger.get_input_port(0))
diagram = builder.Build()

# Create the simulator.
simulator = Simulator(diagram)

# Set the initial conditions, x(0).
state = simulator.get_mutable_context().get_mutable_state()\
                 .get_mutable_continuous_state().get_mutable_vector()
state.SetFromVector([0.9])

# Simulate for 10 seconds.
simulator.StepTo(10)

# Plot the results.
plt.plot(logger.sample_times(), logger.data().transpose())
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()
