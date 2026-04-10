from server.cloud_env import CloudEnv

env = CloudEnv()
state = env.reset()

total_reward = 0

print("[START] task=cloud_orchestration", flush=True)

for i in range(10):
    # simple logic (baseline agent)
    if state["cpu_usage"] > 80:
        action = "scale_up"
    elif state["cpu_usage"] < 40:
        action = "scale_down"
    else:
        action = "do_nothing"

    state, reward, done, _ = env.step(action)
    total_reward += reward

    print(f"[STEP] step={i+1} reward={reward}", flush=True)

score = total_reward / 10
print(f"[END] task=cloud_orchestration score={score} steps=10", flush=True)
