from app import text_to_morse, morse_to_text

def testcase(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f"[PASS] {func.__name__} -> {result!r}")
            return result
        except AssertionError as e:
            print(f"[FAIL] {func.__name__} {e}")
        except Exception as e:
            print(f"[ERROR] {func.__name__} {type(e).__name__}: {e}")
    return wrapper


@testcase
def test_text_to_morse():
    assert text_to_morse("SOS") == "... --- ..."
    assert text_to_morse("Hello") == ".... . .-.. .-.. ---"
    assert text_to_morse("HELLO WORLD") == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

@testcase
def test_morse_to_text():
    assert morse_to_text("... --- ...") == "SOS"
    assert morse_to_text(".... . .-.. .-.. ---") == "HELLO"
    assert morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -..") == "HELLO WORLD"

if __name__ == "__main__":
    test_text_to_morse()
    test_morse_to_text()
