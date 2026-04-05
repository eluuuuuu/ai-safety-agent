from agent import run_agent

def test_safe_input():
    response = run_agent("Hello, translate this to French.")
    assert response is not None
    assert isinstance(response, str)