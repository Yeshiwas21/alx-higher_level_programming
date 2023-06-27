#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t list_size, alloc_size, i;
	const char *type_name;
	PyListObject *list_obj = (PyListObject *)p;
	PyVarObject *var_obj = (PyVarObject *)p;

	list_size = var_obj->ob_size;
	alloc_size = list_obj->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0) {
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", alloc_size);

	for (i = 0; i < list_size; i++) {
		type_name = list_obj->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);
		if (strcmp(type_name, "bytes") == 0) {
			print_python_bytes(list_obj->ob_item[i]);
		} else if (strcmp(type_name, "float") == 0) {
			print_python_float(list_obj->ob_item[i]);
		}
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes_size, i;
	PyBytesObject *bytes_obj = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes_obj->ob_sval);

	bytes_size = (((PyVarObject *)p)->ob_size >= 10) ? 10 : ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", bytes_size);
	for (i = 0; i < bytes_size; i++) {
		printf("%02hhx", bytes_obj->ob_sval[i]);
		if (i != bytes_size - 1) {
			printf(" ");
		}
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0) {
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}

