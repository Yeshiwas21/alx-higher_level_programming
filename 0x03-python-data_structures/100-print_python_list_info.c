#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints information about a Python list object.
 * @p: Pointer to a Python object.
 * Return: Void.
 */
void print_python_list_info(PyObject *p)
{
    long int size, memory, index;
    PyObject *item;

    size = PyList_Size(p);
    memory = ((PyListObject *)p)->memory;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", memory);

    for (index = 0; index < size; index++)
    {
        item = PyList_GetItem(p, index);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

