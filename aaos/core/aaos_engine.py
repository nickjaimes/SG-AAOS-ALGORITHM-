from .metrics_model import SystemMetrics
from .system_adapter import get_system_metrics
from .actions import plan_actions


class AAOSEngine:
    """
    Core AI-Assisted OS Engine.

    It does not modify the OS itself.
    It:
      - observes metrics
      - decides optimization suggestions/actions
      - can be wired to TRINITY/QNSF later
    """

    def __init__(self, policy: dict):
        self.policy = policy

    def tick(self):
        """
        Execute one AAOS cycle.
        Returns:
          snapshot dict with metrics and recommended actions.
        """
        metrics = get_system_metrics()
        actions = plan_actions(metrics, self.policy)

        return {
            "metrics": metrics,
            "actions": actions,
        }
