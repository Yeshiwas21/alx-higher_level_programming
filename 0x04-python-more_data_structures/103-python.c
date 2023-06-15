#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <string.h>

/**
 * print_python_bytes - print information about Python byte objects
 * @p: pointer to PyObject p
 * Return: void
 */
void print_python_bytes(PyObject *p) {
    char *str;
    int i;
    ssize_t size;

    printf("[.] bytes object info\n");
    
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    
    PyBytes_AsStringAndSize(p, &str, &size);
    printf("  size: %li\n", size);
    printf("  trying string: %s\n", str);
    
    if (size > 10) {
        size = 10;
    } else {
        size++;
    }
    
    printf("  first %li bytes: ", size);
    
    for (i = 0; i < size - 1; i++) {
        printf("%02hhx ", str[i]);
    }
    
    printf("%02hhx\n", str[i]);
}

/**
 * print_python_list - print information about Python lists
 * @p: PyObject pointer
 * Return: void
 */
void print_python_list(PyObject *p) {
    int i, size, allocated;
    const char *dataType;
    PyListObject *list = (PyListObject *)p;
    
    size = PyList_Size(p);
    allocated = list->allocated;
    
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %i\n", size);
    printf("[*] Allocated = %i\n", allocated);
    
    for (i = 0; i < size; i++) {
        dataType = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, dataType);
        
        if (strcmp(dataType, "bytes") == 0) {
            print_python_bytes(list->ob_item[i]);
        }
    }
}

