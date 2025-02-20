def function_with_uncommon_error_solution(a, b):
    if a == 0:
        return float('inf') # Or handle the error in a way that is appropriate for the application.  For example, you might return a default value, raise a custom exception, or log the error.
    return a + b