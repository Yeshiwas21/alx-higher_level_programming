#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <string.h>

/**
 * print_python_bytes - Print information about Python byte objects
 * @obj: Pointer to PyObject object
 * Return: void
 */
void print_python_bytes(PyObject *obj) {
    char *data;
    int i;
    ssize_t size;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(obj)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(obj, &data, &size);
    printf("  size: %li\n", size);
    printf("  trying string: %s\n", data);

    if (size > 10) {
        size = 10;
    } else {
        size++;
    }

    printf("  first %li bytes: ", size);

    for (i = 0; i < size - 1; i++) {
        printf("%02hhx ", data[i]);
    }

    printf("%02hhx\n", data[i]);
}

/**
 * print_python_list - Print information about Python lists
 * @obj: PyObject pointer
 * Return: void
 */
void print_python_list(PyObject *obj) {
    int i, list_size, allocated;
    const char *data_type;
    PyListObject *list_obj = (PyListObject *)obj;

    list_size = PyList_Size(obj);
    allocated = list_obj->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %i\n", list_size);
    printf("[*] Allocated = %i\n", allocated);

    for (i = 0; i < list_size; i++) {
        data_type = (list_obj->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, data_type);

        if (strcmp(data_type, "bytes") == 0) {
            print_python_bytes(list_obj->ob_item[i]);
        }
    }
}
