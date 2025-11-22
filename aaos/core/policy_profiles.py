def get_policy_profile(name: str) -> dict:
    """
    AAOS policy profiles describe how aggressive the system should be.

    - 'boost'      : max responsiveness, more frequent actions
    - 'balanced'   : normal usage, gentle optimizations
    - 'eco'        : energy & quiet priority
    """

    profiles = {
        "boost": {
            "scan_interval_sec": 3,
            "max_background_cpu": 0.25,
            "mem_pressure_threshold": 0.7,
            "aggressiveness": 0.9,
        },
        "balanced": {
            "scan_interval_sec": 5,
            "max_background_cpu": 0.4,
            "mem_pressure_threshold": 0.8,
            "aggressiveness": 0.6,
        },
        "eco": {
            "scan_interval_sec": 8,
            "max_background_cpu": 0.5,
            "mem_pressure_threshold": 0.9,
            "aggressiveness": 0.4,
        },
    }

    return profiles.get(name, profiles["balanced"])
