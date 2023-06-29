from testlib import *
import re

regex = re.compile(r"Hello world!")
stdout_verifier = verifier.MatchRegex(regex)

# Really, all we're doing here is setting up two runs:
# ./build/ALL/gem5.opt materials/testlib/hello-world.py --isa X86
# ./build/ALL/gem5.opt materials/testlib/hello-world.py --isa ARM
#
# Then compare the stdout using the regex.
# To do this we use the `gem5_verify_config` function, which has various
# parameters to specify these two tests.
for isa in ("X86", "ARM"):
    gem5_verify_config(
        # The name of the test. This must be unique or an error is given.
        name=f"test-hello-{isa}",
        # Here we specify the verifier. Where we compare to some ground truth.
        # Here we compare the stdout to a regex.
        verifiers=(stdout_verifier,),
        # The config script to run.
        config=joinpath(
            config.base_dir, "materials", "testlib", "hello-world.py"
        ),
        # The arguments to pass to the config file.
        config_args=[
            "--isa",
            isa,
        ],
        # This will ensure the "ALL/gem5" is compiled. You can specify other
        # targets like "X86/gem5.opt" or "ARM/gem5.opt" to run the tests.
        # To reduce required compilations, we only allow for "ALL/gem5.opt"
        #
        valid_isas=(constants.all_compiled_tag,),
        valid_hosts=constants.supported_hosts,
        # 'constants.quick_tag' for CI, 'constants.long_tag' for Daily,
        # 'constants.very_long_tag' for Weekly.
        length=constants.quick_tag,
        # If needed, we can specify the coherence protocol to use.
        # protocol="MI_example",
    )
