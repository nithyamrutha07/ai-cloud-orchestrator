def easy_task(state):
    cpu = state["cpu_usage"]
    if 40 <= cpu <= 70:
        return 1
    return 0


def medium_task(state):
    if state["cpu_usage"] < 80 and state["servers"] <= 3:
        return 1
    return 0


def hard_task(state):
    cpu = state["cpu_usage"]
    servers = state["servers"]

    if 40 <= cpu <= 70 and servers <= 3:
        return 1
    return 0