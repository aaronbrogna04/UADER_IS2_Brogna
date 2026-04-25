import unittest
from rpn import eval_rpn, RPNError, main
import math
from unittest.mock import patch


class TestRPN(unittest.TestCase):

    # ------------------------
    # OPERACIONES BÁSICAS
    # ------------------------
    def test_operaciones(self):
        self.assertEqual(eval_rpn("3 4 +".split()), 7)
        self.assertEqual(eval_rpn("5 1 2 + 4 * + 3 -".split()), 14)
        self.assertEqual(eval_rpn("2 3 4 * +".split()), 14)
        self.assertEqual(eval_rpn("8 2 /".split()), 4)

    def test_floats_negativos(self):
        self.assertAlmostEqual(eval_rpn("2.5 2 *".split()), 5.0)
        self.assertEqual(eval_rpn("-3 2 *".split()), -6)

    # ------------------------
    # FUNCIONES
    # ------------------------
    def test_funciones(self):
        self.assertEqual(eval_rpn("9 sqrt".split()), 3)
        self.assertEqual(eval_rpn("100 log".split()), 2)
        self.assertAlmostEqual(eval_rpn("2.718281828 ln".split()), 1, places=3)
        self.assertEqual(eval_rpn("2 3 yx".split()), 8)
        self.assertEqual(eval_rpn("2 1/x".split()), 0.5)
        self.assertEqual(eval_rpn("2 10x".split()), 100)
        self.assertAlmostEqual(eval_rpn("1 ex".split()), math.e)

    # ------------------------
    # TRIGONOMETRÍA
    # ------------------------
    def test_trig(self):
        self.assertAlmostEqual(eval_rpn("90 sin".split()), 1, places=5)
        self.assertAlmostEqual(eval_rpn("0 cos".split()), 1, places=5)
        self.assertAlmostEqual(eval_rpn("45 tg".split()), 1, places=5)

    def test_trig_inversas(self):
        self.assertAlmostEqual(eval_rpn("1 asin".split()), 90, places=5)
        self.assertAlmostEqual(eval_rpn("1 acos".split()), 0, places=5)
        self.assertAlmostEqual(eval_rpn("1 atg".split()), 45, places=5)

    # ------------------------
    # CONSTANTES
    # ------------------------
    def test_constantes(self):
        self.assertAlmostEqual(eval_rpn("p".split()), math.pi)
        self.assertAlmostEqual(eval_rpn("e".split()), math.e)
        self.assertAlmostEqual(eval_rpn("j".split()), (1 + 5**0.5) / 2)

    # ------------------------
    # PILA
    # ------------------------
    def test_pila(self):
        self.assertEqual(eval_rpn("3 dup *".split()), 9)
        self.assertEqual(eval_rpn("3 4 swap -".split()), 1)
        self.assertEqual(eval_rpn("3 4 drop".split()), 3)
        self.assertEqual(eval_rpn("3 clear 5".split()), 5)

    # ------------------------
    # MEMORIA
    # ------------------------
    def test_memoria(self):
        self.assertEqual(eval_rpn("5 01 sto 01 rcl".split()), 5)
        self.assertEqual(eval_rpn("5 01 sto 7 02 sto 01 rcl 02 rcl +".split()), 12)

    # ------------------------
    # ERRORES (TRY/EXCEPT)
    # ------------------------
    def test_division_por_cero(self):
        try:
            eval_rpn("3 0 /".split())
            self.fail()
        except RPNError as e:
            self.assertIn("cero", str(e).lower())

    def test_token_invalido(self):
        try:
            eval_rpn("2 3 &".split())
            self.fail()
        except RPNError as e:
            self.assertIn("token", str(e).lower())

    def test_pila_insuficiente(self):
        try:
            eval_rpn("+".split())
            self.fail()
        except RPNError as e:
            self.assertIn("pila", str(e).lower())

    def test_pila_final(self):
        try:
            eval_rpn("2 3".split())
            self.fail()
        except RPNError as e:
            self.assertIn("exactamente", str(e).lower())

    def test_sqrt_negativo(self):
        try:
            eval_rpn("-1 sqrt".split())
            self.fail()
        except RPNError:
            pass

    def test_log_invalido(self):
        try:
            eval_rpn("0 log".split())
            self.fail()
        except RPNError:
            pass

    def test_ln_invalido(self):
        try:
            eval_rpn("-1 ln".split())
            self.fail()
        except RPNError:
            pass

    def test_swap_error(self):
        try:
            eval_rpn("1 swap".split())
            self.fail()
        except RPNError:
            pass

    def test_dup_error(self):
        try:
            eval_rpn("dup".split())
            self.fail()
        except Exception:
            pass

    def test_drop_error(self):
        try:
            eval_rpn("drop".split())
            self.fail()
        except RPNError:
            pass

    def test_memoria_invalida(self):
        try:
            eval_rpn("5 10 sto".split())
            self.fail()
        except RPNError:
            pass

    def test_trig_fuera_dominio(self):
        try:
            eval_rpn("2 asin".split())
            self.fail()
        except Exception:
            pass

    # ------------------------
    # MAIN (IMPORTANTE)
    # ------------------------
    def test_main_argumentos(self):
        with patch("sys.argv", ["rpn.py", "3", "4", "+"]):
            main()

    def test_main_input(self):
        with patch("builtins.input", return_value="3 4 +"):
            with patch("sys.argv", ["rpn.py"]):
                main()


if __name__ == "__main__":
    unittest.main()