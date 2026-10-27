"""Replace one hook at a time, then run the corresponding project with --student.

These intentionally simple implementations are working starting points, not
solutions to the research questions. Do not read simulator-private state.
"""


def choose_path(observation, rng):
    """P1: return a path index. Try hysteresis or delayed measurements."""
    return rng.randrange(len(observation))


def forecast_features(history):
    """P2: return a fixed-length numeric vector using only the supplied history."""
    return [history[-1]]


def allocate(observation):
    """P3: return an action index 0..4 for class-0 shares .1,.3,.5,.7,.9."""
    return 2


def agent_action(observation):
    """P4: return one tool name. Only observation['results'] exposes tool data."""
    return "verify" if "restart_service" in observation["results"] else "restart_service"
