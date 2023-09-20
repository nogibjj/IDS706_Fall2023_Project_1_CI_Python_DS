import base # noqa: F401
from fortune500_analyze import run

def test_fortune500_analyze():
    assert run() == 25131
    
if __name__ == "__main__":
    test_fortune500_analyze()
    print("all tests in test_script passed!")