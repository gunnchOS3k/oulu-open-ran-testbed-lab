from gunnchos_ran.xapp_policy_stub import policy


def test_policy():
    assert policy({"load": 0.5})["slice"] == "eMBB"
