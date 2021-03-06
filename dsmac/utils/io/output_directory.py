from logging import Logger

import os
import shutil

from dsmac.scenario.scenario import Scenario


def create_output_directory(
        scenario: Scenario,
        run_id: str,
        logger: Logger = None,
):
    """Create output directory for this run.

    Side effect: Adds the current output directory to the scenario object!

    Parameters:
    -----------

    scenario : ~dsmac.scenario.scenario.Scenario

    run_id : int
    """
    if scenario.output_dir:
        output_dir = os.path.join(
            scenario.output_dir,
            "run_%s" % (run_id),
        )
    else:
        return ""
    if os.path.exists(output_dir):
        move_to = output_dir + ".OLD"
        while (os.path.exists(move_to)):
            move_to += ".OLD"
        shutil.move(output_dir, move_to)
        if logger is not None:
            logger.warning("Output directory \"%s\" already exists! "
                           "Moving old folder to \"%s\".",
                           output_dir, move_to)
    scenario.output_dir_for_this_run = output_dir
    return output_dir

