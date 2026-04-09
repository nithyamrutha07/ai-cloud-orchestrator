from server.cloud_env import CloudEnv

env = CloudEnv()

state = env.reset()

for i in range(10):
    # simple logic (baseline agent)
    if state["cpu_usage"] > 80:
        action = "scale_up"
    elif state["cpu_usage"] < 40:
        action = "scale_down"
    else:
        action = "do_nothing"

    state, reward, done, _ = env.step(action)

    print(f"Step {i}:")
    print("State:", state)
    print("Reward:", reward)
    print("-" * 30)