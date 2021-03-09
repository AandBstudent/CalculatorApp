"""
Unit tests using pytest for the calculator app
"""
import calculator

class TestCalculator:
    
    def test_add(self):
        assert 6 == calculator.add(1,5)
        
    def test_subtract(self):
        assert 2 == calculator.subtract(4,2)
        
    def test_multipy(self):
        assert 9 == calculator.multiply(3,3)