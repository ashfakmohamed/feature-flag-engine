import pytest

from feature_flag_engine import FeatureFlag, evaluate


def test_disabled_allowlist_and_rollout_paths():
    assert not evaluate(FeatureFlag("new-ui", enabled=False), "a").enabled
    assert evaluate(FeatureFlag("new-ui", rollout_percentage=0, allowed_users=frozenset({"a"})), "a").enabled
    assert not evaluate(FeatureFlag("new-ui", rollout_percentage=0), "b").enabled


def test_rejects_invalid_percentage():
    with pytest.raises(ValueError):
        FeatureFlag("bad", rollout_percentage=101)
