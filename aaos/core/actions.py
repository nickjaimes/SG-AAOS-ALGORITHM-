def plan_actions(metrics, policy):
    """
    Pure decision logic:
    - Takes metrics + policy
    - Returns list of suggested actions (strings or dicts).
    """

    actions = []

    # Example 1: Too much background CPU
    if metrics.cpu_background > policy["max_background_cpu"]:
        actions.append("lower_priority:background_heavy_processes")

    # Example 2: High memory pressure
    if metrics.mem_used_fraction > policy["mem_pressure_threshold"]:
        actions.append("suggest_close:top_memory_hogs")

    # Example 3: Disk IO spike
    # (Here we only flag; future: coordinate scheduling)
    # if metrics.disk_io_rate > SOME_THRESHOLD: ...

    return actions
