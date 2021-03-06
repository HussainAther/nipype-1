# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import Threshold


def test_Threshold_inputs():
    input_map = dict(absolute_threshold_value=dict(argstr='-abs %s',
    ),
    args=dict(argstr='%s',
    ),
    debug=dict(argstr='-debug',
    position=1,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    invert=dict(argstr='-invert',
    position=1,
    ),
    out_filename=dict(argstr='%s',
    genfile=True,
    position=-1,
    ),
    percentage_threshold_value=dict(argstr='-percent %s',
    ),
    quiet=dict(argstr='-quiet',
    position=1,
    ),
    replace_zeros_with_NaN=dict(argstr='-nan',
    position=1,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = Threshold.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Threshold_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Threshold.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
