Considere el siguiente problema:

	Escriba un algoritmo que dada una matriz lineal de números enteros, encuentre el número que 
	aparece más veces teniendo un número de apariciones impar.

	Ejemplo:

		[ 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1 ] 
		
    Apariciones:

        	1  -> 10 (par)
        	10 -> 1 (impar)

    Solución:

       	 10


    Ejemplo:

		[ 1, 0, 5, 5, 5] 
		
    Apariciones:

        	1  -> 1 (impar)
        	0  -> 1 (impar)
            5  -> 3 (impar)

    Solución:

       	 5

    En la carpeta 'src/kata.py' se encuentra el fichero con la
    definición de nuestros métodos vacíos.
    En la carpeta 'tests/kata_test.py' se encuentra el fichero 
    con la suite de test.

    El modus operandi de trabajo es el siguiente:
    
    Debes 'forkear' el proyecto a tu cuenta.
    Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    Puedes trabajar en local y subir la solución haciendo un PR a nuestro repositorio.
    Cuando se envíe la PR final, debes indicar el tiempo de dedicación y los intentos que has hecho.
    También puedes añadir un comentario para dar cualquier tipo de feedback.
    
    En caso de duda, revisa en el apartado de 'Referencias'.


    [TestSuite]

    tests/test_kata.py::Test_kata::test_apply_1 PASSED                       [  6%]
    tests/test_kata.py::Test_kata::test_apply_10 PASSED                      [ 13%]
    tests/test_kata.py::Test_kata::test_apply_11 PASSED                      [ 20%]
    tests/test_kata.py::Test_kata::test_apply_12 PASSED                      [ 26%]
    tests/test_kata.py::Test_kata::test_apply_13 PASSED                      [ 33%]
    tests/test_kata.py::Test_kata::test_apply_14 PASSED                      [ 40%]
    tests/test_kata.py::Test_kata::test_apply_15 PASSED                      [ 46%]
    tests/test_kata.py::Test_kata::test_apply_2 PASSED                       [ 53%]
    tests/test_kata.py::Test_kata::test_apply_3 PASSED                       [ 60%]
    tests/test_kata.py::Test_kata::test_apply_4 PASSED                       [ 66%]
    tests/test_kata.py::Test_kata::test_apply_5 PASSED                       [ 73%]
    tests/test_kata.py::Test_kata::test_apply_6 PASSED                       [ 80%]
    tests/test_kata.py::Test_kata::test_apply_7 PASSED                       [ 86%]
    tests/test_kata.py::Test_kata::test_apply_8 PASSED                       [ 93%]
    tests/test_kata.py::Test_kata::test_apply_9 PASSED                       [100%]

    
## Referencias

* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)
