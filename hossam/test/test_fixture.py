import pytest

@pytest.fixture(scope='module')
def stupe_DB_connection():
    print("\nopencontion\n")
    yield
    print("\nclosecontion\n")


def test_insert_data(stupe_DB_connection):
    print("insert data test")


def test_delete_data(stupe_DB_connection):
    print("delete data test")


def test_update_data(stupe_DB_connection):
    print("update data test")
