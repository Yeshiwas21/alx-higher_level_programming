#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
  * print_python_list - prints info about Python list object if it is valid
  * @p: a Python object that is being passed as an argument 
  *
  * Return: Nothing.
  */
void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, typeName);
    }
}

/**
  * print_python_bytes - prints info about Python byte object if it is valid
  * @p: a Python object that is being passed as an argument
  *
  * Return: Nothing.
  */
void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] Bytes object info\n");
    printf("  [.] Size: %zd\n", size);
    printf("  [.] Trying string: %s\n", PyBytes_AsString(p));

    if (size > 10)
        size = 10;
    printf("  [.] First %zd bytes: ", size);
    for (Py_ssize_t i = 0; i < size; i++) {
        printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

/**
  * print_python_float - prints info about Python float object if it is valid
  * @p: a Python object that is being passed as an argument
  *
  * Return: Nothing.
  */
void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[ERROR] Invalid PyFloatObject\n");
        return;
    }

    double value = PyFloat_AsDouble(p);
    printf("[.] Float object info\n");
    printf("  [.] Value: %f\n", value);
}
