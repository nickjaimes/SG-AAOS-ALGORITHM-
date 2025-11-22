(Concept only – real implementation will use psutil and OS commands)

import psutil

def get_system_metrics() -> "SystemMetrics":
    """
    Collects basic metrics using psutil and simple heuristics.
    Foreground process detection is OS-specific and may be stubbed initially.
    """
    cpu_total = psutil.cpu_percent(interval=0.1) / 100.0
    mem = psutil.virtual_memory()
    mem_used_fraction = mem.used / mem.total

    processes = []
    for p in psutil.process_iter(["name", "cpu_percent", "memory_info"]):
        try:
            info = p.info
            processes.append((
                info.get("name") or "unknown",
                info.get("cpu_percent", 0.0) / 100.0,
                (info.get("memory_info").rss if info.get("memory_info") else 0) / (1024**3),
                False,  # foreground detection placeholder
            ))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Simple split: top N as "foreground-ish"
    processes_sorted = sorted(processes, key=lambda x: x[1], reverse=True)
    top_processes = processes_sorted[:10]

    cpu_foreground = sum(p[1] for p in top_processes[:2])
    cpu_background = max(0.0, cpu_total - cpu_foreground)

    # Disk IO rate placeholder
    disk_io_rate = psutil.disk_io_counters().read_bytes + psutil.disk_io_counters().write_bytes

    return SystemMetrics(
        cpu_total=cpu_total,
        cpu_foreground=cpu_foreground,
        cpu_background=cpu_background,
        mem_used_fraction=mem_used_fraction,
        disk_io_rate=float(disk_io_rate),
        top_processes=top_processes,
    )
  
