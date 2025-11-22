from dataclasses import dataclass


@dataclass
class SystemMetrics:
    cpu_total: float           # 0.0 - 1.0
    cpu_foreground: float      # estimated share of active app
    cpu_background: float      # rest of CPU load
    mem_used_fraction: float   # 0.0 - 1.0
    disk_io_rate: float        # relative or normalized
    top_processes: list        # list of (name, cpu, mem, is_foreground)
