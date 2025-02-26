import functools
import datetime

def log(filename=None):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"{timestamp} - Function {func.__name__}"

            try:
                result = func(*args, **kwargs)
                log_message += f" executed successfully. Result: {result}\n"
            except Exception as e:
                log_message += f" encountered an error: {type(e).__name__} - {str(e)}. Inputs: {args}, {kwargs}\n"
                raise

            if filename:
                try:
                    with open(filename, "a") as f:
                        f.write(log_message)
                except Exception as e:
                    print(f"Error writing to file {filename}: {e}")
            else:
                print(log_message, end="")

            if 'e' in locals():
                raise

            return result

        return wrapper
    return decorator
