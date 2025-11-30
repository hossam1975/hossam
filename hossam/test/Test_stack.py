import pytest
from src.stack import Stack as stc

class TestStack:

    def test_push(self):
        s = stc()       # ← إنشاء object من ال Stack
        s.push(5)
        s.push(10)
        s.push(15)
        s.push(20)

        assert s.is_empty() == False
        assert s.get_stack_siz() == 4
        assert s.get_peek_element() == 20
        assert s.get_all_items() == [5, 10, 15, 20]

    def test_pop(self):
        s = stc()       # ← إنشاء object جديد
        s.push(5)
        s.push(10)
        s.push(15)
        s.push(20)

        assert s.is_empty() == False
        assert s.get_stack_siz() == 4
        assert s.pop() == 20
        assert s.get_stack_siz() == 3
        assert s.get_peek_element() == 15
        assert s.get_all_items() == [5, 10, 15]



    






      
