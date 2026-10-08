import hashlib
from dataclasses import dataclass, field


@dataclass(frozen=True)
class FeatureFlag:
    name: str
    enabled: bool = True
    rollout_percentage: int = 100
    allowed_users: frozenset[str] = field(default_factory=frozenset)

    def __post_init__(self) -> None:
        if not 0 <= self.rollout_percentage <= 100:
            raise ValueError("rollout_percentage must be between zero and 100")


@dataclass(frozen=True)
class Evaluation:
    enabled: bool
    reason: str


def evaluate(flag: FeatureFlag, user_id: str) -> Evaluation:
    if not flag.enabled:
        return Evaluation(False, "flag disabled")
    if user_id in flag.allowed_users:
        return Evaluation(True, "user allowlist")
    digest = hashlib.sha256(f"{flag.name}:{user_id}".encode()).hexdigest()
    bucket = int(digest[:8], 16) % 100
    enabled = bucket < flag.rollout_percentage
    return Evaluation(enabled, f"rollout bucket {bucket}")
