"""Prefix-cache poisoning for replay scenarios.

Provides compute_scenario_lcp() and poison_task_execution() used by
the replay engine. Cache-defeat implementations are loaded from
extension modules when available; otherwise these return no-op values
(LCP=0, task unchanged) which is correct for allwarm cache mode.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from agentic_swarm_bench.scenarios.registry import Task




def compute_scenario_lcp(tasks: list[Task]) -> int:
    return 0


def poison_task_execution(
    task: Task,
    lcp_len: int,
    execution_index: int,
) -> Task:
    return task
