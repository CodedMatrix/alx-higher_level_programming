#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    // Check if the input is a string
    if (!PyUnicode_Check(p))
    {
        fprintf(stderr, "[.] string object info\n[ERROR] Invalid String Object\n");
        return;
    }

    // Get the string representation and length
    const char *str = PyUnicode_AsUTF8(p);
    Py_ssize_t length = PyUnicode_GetLength(p);
    const char *type;

    // Determine the type of the string (ASCII or Unicode)
    if (PyUnicode_IS_COMPACT_ASCII(p))
        type = "compact ascii";
    else
        type = "compact unicode object";

    // Print the information
    printf("[.] string object info\n");
    printf("  type: %s\n", type);
    printf("  length: %zd\n", length);
    printf("  value: %s\n", str);
}

