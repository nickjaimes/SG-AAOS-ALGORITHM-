---

## 🔧 2. Tiny Code Helper: TRINITY Adapter (Optional File)

You can add a small helper in `aaos/core/trinity_adapter.py`:

```python
from aaos.core.policy_profiles import get_policy_profile
from aaos.core.aaos_engine import AAOSEngine


class TrinityAAOSAdapter:
    """
    Adapter layer between TRINITY AI and AAOS Engine.
    TRINITY gives: policy name / mode
    Adapter returns: AAOS snapshot for TRINITY to inspect.
    """

    def __init__(self, trinity_policy_source):
        """
        trinity_policy_source: callable that returns dict, e.g.
        {"aaos_policy": "balanced"}
        """
        self.trinity_policy_source = trinity_policy_source

    def run_tick(self):
        policy_info = self.trinity_policy_source() or {}
        policy_name = policy_info.get("aaos_policy", "balanced")

        policy = get_policy_profile(policy_name)
        engine = AAOSEngine(policy=policy)

        snapshot = engine.tick()
        return snapshot


Then TRINITY side can simply call:

adapter = TrinityAAOSAdapter(trinity_policy_source=get_trinity_policy)
snapshot = adapter.run_tick()
trinity.handle_aaos_snapshot(snapshot)

