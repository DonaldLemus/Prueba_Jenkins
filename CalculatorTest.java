import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {

    private Calculator calculator;

    @BeforeEach
    public void setUp() {
        calculator = new Calculator();
    }

    @Test
    public void testAdd() {
        assertEquals(15, calculator.add(10, 5));
        assertEquals(0, calculator.add(-1, 1));
    }

    @Test
    public void testSubtract() {
        assertEquals(5, calculator.subtract(10, 5));
        assertEquals(-2, calculator.subtract(-1, 1));
    }

    @Test
    public void testMultiply() {
        assertEquals(50, calculator.multiply(10, 5));
        assertEquals(-1, calculator.multiply(-1, 1));
    }

    @Test
    public void testDivide() {
        assertEquals(2, calculator.divide(10, 5));
        assertThrows(IllegalArgumentException.class, () -> calculator.divide(10, 0));
    }

    @Test
    public void testSquareRoot() {
        assertEquals(5, calculator.squareRoot(25));
        assertThrows(IllegalArgumentException.class, () -> calculator.squareRoot(-1));
    }
}

