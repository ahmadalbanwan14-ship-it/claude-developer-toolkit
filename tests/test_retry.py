import pytest

import claude_toolkit.retry as retry_module
from claude_toolkit.retry import retry


def test_retry_eventually_returns(monkeypatch):
    monkeypatch.setattr(retry_module.time, "sleep", lambda _: None)
    attempts = {"count": 0}

    @retry(max_attempts=3, base_delay=0)
    def flaky():
        attempts["count"] += 1
        if attempts["count"] < 3:
            raise RuntimeError("temporary")
        return "ok"

    assert flaky() == "ok"
    assert attempts["count"] == 3


def test_retry_raises_after_limit(monkeypatch):
    monkeypatch.setattr(retry_module.time, "sleep", lambda _: None)

    @retry(max_attempts=2, base_delay=0)
    def always_fails():
        raise ValueError("nope")

    with pytest.raises(ValueError):
        always_fails()


def test_retry_validates_arguments():
    with pytest.raises(ValueError):
        retry(max_attempts=0)

    with pytest.raises(ValueError):
        retry(base_delay=-1)
