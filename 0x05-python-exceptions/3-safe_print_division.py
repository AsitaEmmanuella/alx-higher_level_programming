#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b

    except ZeroDivisionError:
        return None
    except Exception as e:
        print("Exception:", e)
        return None
    else:
        return result

    finally:
        if "result" in locals():
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")
