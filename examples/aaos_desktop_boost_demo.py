"""
AAOS Desktop Boost Demo

Simulates a single AAOS tick and prints recommended optimizations.
"""

from aaos.core.aaos_engine import AAOSEngine
from aaos.core.policy_profiles import get_policy_profile


def main():
    policy = get_policy_profile("balanced")
    engine = AAOSEngine(policy=policy)

    snapshot = engine.tick()

    print("\n[AAOS SNAPSHOT]")
    print("CPU total:      ", snapshot["metrics"].cpu_total)
    print("CPU foreground: ", snapshot["metrics"].cpu_foreground)
    print("CPU background: ", snapshot["metrics"].cpu_background)
    print("Mem used frac:  ", snapshot["metrics"].mem_used_fraction)
    print("\nRecommended actions:")
    for act in snapshot["actions"]:
        print("  -", act)
    print()


if __name__ == "__main__":
    main()
