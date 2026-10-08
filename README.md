# Feature Flag Engine

A deterministic, dependency-free feature flag evaluator with global disable, user allowlists, and percentage rollout.

## Highlights

- Stable SHA-256 user bucketing
- Explainable evaluation reasons
- Explicit rollout validation
- Suitable as an embedded backend policy primitive

```python
from feature_flag_engine import FeatureFlag, evaluate

decision = evaluate(FeatureFlag("assistant-v2", rollout_percentage=15), user_id)
```

Production platforms should add persistent configuration, tenant isolation, audit logs, and administrative controls.

No license has been selected; all rights are reserved.
