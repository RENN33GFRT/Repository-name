import functools


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args=}, {kwargs=}\n"
                if filename:
                    try:
                        with open(filename, "a") as f:
                            f.write(log_message)
                    except Exception as file_e:
                        print(f"Error writing to file {filename}: {file_e}")
                else:
                    print(log_message, end="")
                raise

            if filename:
                try:
                    with open(filename, "a") as f:
                        f.write(log_message)
                except Exception as file_e:
                    print(f"Error writing to file {filename}: {file_e}")
            else:
                print(log_message, end="")

            return result

        return wrapper

    return decorator


"n"
