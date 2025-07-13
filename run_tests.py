import os


def execute_pytest_test(test_name):
    os.system(f"pytest -v -k \"{test_name}\"")


def print_test_options():
    print(" Bienvenido a las pruebas de EDA ".center(80, "="))
    print("1. Todas las estructuras")
    print("2. Listas")
    print("     2.A Lista de arreglos")
    print("     2.B Lista encadenadas")
    print("3. Colas (Queues)")
    print("4. Pilas (Stacks)")
    print("5. Métodos de Ordenamiento Iterativos")
    print("7. Mapas")
    print("     7.A Mapas con manejo linear probing")
    print("     7.B Mapas con manejo Separate Chaining")
    print("8. Árboles binarios de búsqueda")
    print("9. Árboles rojo negro")
    print("0. Salir")


def execute_all_tests():
    """Ejecuta todas las pruebas disponibles"""
    execute_list_tests()
    execute_queue_tests()
    execute_stack_tests()


def execute_list_tests(input_option="2"):
    """Ejecuta pruebas relacionadas con listas"""
    tests_names = []
    if input_option.lower() == "2.a" or input_option == "2":
        tests_names.append("test_array_list")
    if input_option.lower() == "2.b" or input_option == "2":
        tests_names.append("test_single_linked_list")
    for test_name in tests_names:
        execute_pytest_test(test_name)


def execute_queue_tests():
    """Ejecuta las pruebas de la cola (queue)"""
    execute_pytest_test("test_queue")


def execute_stack_tests():
    """Ejecuta las pruebas de la pila (stack)"""
    execute_pytest_test("test_stack")
    
def execute_sorting_tests():
    tests_names = []
    tests_names.append("test_iterative_sort_array_list")
    tests_names.append("test_iterative_sort_single_linked_list")
    
    for test_name in tests_names:
        execute_pytest_test(test_name)

def execute_map_tests(input_option="7"):
    """Ejecuta pruebas relacionadas con mapas"""
    tests_names = []
    if input_option.lower() == "7.a" or input_option == "7":
        tests_names.append("test_map_linear_probing")
    if input_option.lower() == "7.b" or input_option == "7":
        tests_names.append("test_map_separate_chaining")
    for test_name in tests_names:
        execute_pytest_test(test_name)

def execute_bst_tests():
    """Ejecuta las pruebas de BST"""
    execute_pytest_test("test_binary_search_tree")
    
def execute_rbt_tests():
    """Ejecuta las pruebas de BST"""
    execute_pytest_test("test_red_black_tree")


if __name__ == "__main__":
    """Menú principal de pruebas"""
    runned = False
    print_test_options()
    input_option = str(input("Ingrese el número de la opción que desea ejecutar: \n"))

    if input_option == "1":
        execute_all_tests()
        runned = True

    if input_option.startswith("2"):
        execute_list_tests(input_option)
        runned = True

    if input_option == "3":
        execute_queue_tests()
        runned = True

    if input_option == "4":
        execute_stack_tests()
        runned = True
        
    if input_option.startswith("5"):
        execute_sorting_tests()
        runned = True
        
    if input_option.startswith("7"):
        execute_map_tests()
        runned = True
    
    if input_option.startswith("8"):
        execute_bst_tests()
        runned = True
        
    if input_option.startswith("9"):
        execute_rbt_tests()
        runned = True

    if input_option == "0":
        print("Saliendo de las pruebas")

    elif not runned:
        print("Opción no válida")

    print(" Gracias por ejecutar las pruebas ".center(80, "="))
