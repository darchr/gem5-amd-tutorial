from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator
from gem5.isas import ISA

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-i",
    "--isa",
    type=str,
    choices=["X86", "ARM"],
    help="The ISA to test.",
)

args = parser.parse_args()

# Obtain the components.
cache_hierarchy = NoCache()
memory = SingleChannelDDR3_1600("1GiB")

isa = None
if args.isa == "X86":
    isa = ISA.X86
elif args.isa == "ARM":
    isa = ISA.ARM
assert isa is not None

processor = SimpleProcessor(cpu_type=CPUTypes.TIMING, isa=isa, num_cores=1)

# Add them to the board.
board = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

# Set the workload.
id = None
if args.isa == "X86":
    id = "x86-hello64-static"
elif args.isa == "ARM":
    id = "arm-hello64-static"
binary = obtain_resource(id)

board.set_se_binary_workload(binary)

# Setup the Simulator and run the simulation.
simulator = Simulator(board=board)
simulator.run()
