from datetime import datetime, timedelta
from app import app, db
from app.models import User, Post

def test_example():
    print("\n")
    print("\nhello!\n")
    assert 1==1

def xtest_example2():
    assert 1==2

if __name__=="__main__":
    test_example()