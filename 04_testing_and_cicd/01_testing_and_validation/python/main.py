names = ["Nick", "Lewis", "Nikos"]

def contains(name, list_of_names):
    if name not in list_of_names:
        return False
    else:
        return True

def get_name(name, list_of_names):
    if name in list_of_names:
        return name
    else:
        return -1

def add_name(name, list_of_names):
    list_of_names.append(name)
    return name

def add_two(num):
    return num + 2

def divide_by_two(num):
    return num / 2

def greeting(name, num):
    message = f"Hello, {name}. It is {num} degrees warmer today than yesterday"
    print(message)
    return message

# ----ここにコードを書いてください----*/
# ----難易度: 富士----

# `my_assert` をここに定義し、以降のテストに使用してください。
def my_assert(expr, msg=None):
    if expr==False:
        if msg is None:
            msg = "Assertion!"
        result = msg 
    else:
        result = False
    return result

# `contains` 用のテスト `test_contains` を作成してください
def test_contains():
    my_assert(contains("a", ["A", "B", "C"])==False)
    my_assert(contains("A", ["A", "B", "C"])==True)
    my_assert(contains(10, ["A", "B", "C"])==False)

# `add_name` 用のテスト `test_add_name` を作成してください
def test_add_name():
    my_assert(add_name("a", ["A", "B", "C"])=="a")
    my_assert(add_name("A", ["A", "B", "C"])=="A")

# `add_two` 用のテスト `test_add_two` を作成してください
def test_add_two():
    my_assert(add_two(1)==3)
    my_assert(add_two(0)==2)
    my_assert(add_two(0.1)==2.1)
    my_assert(add_two(-2)==0)

# `divide_by_two` 用のテスト `test_divide_by_two` を作成してください
def test_divide_by_two():
    my_assert(divide_by_two(2)==1)
    my_assert(divide_by_two(1)==0.5)
    my_assert(divide_by_two(0)==0)
    my_assert(divide_by_two(0.1)==0.05)
    my_assert(divide_by_two(-1)==-0.5)
    my_assert(divide_by_two(-2)==-1)

# `greeting` 用のテスト `test_greeting` を作成してください
def test_greeting():
    my_assert(greeting('Dan', 4)=='Hello, Dan. It is 4 degrees warmer today than yesterday')
    my_assert(greeting(10, 4)=='Hello, 10. It is 4 degrees warmer today than yesterday')
    my_assert(greeting(10, 'Dan')=='Hello, 10. It is Dan degrees warmer today than yesterday')

# ----難易度: キリマンジャロ----

# `my_assert` 用のテスト `test_my_assert_false` を作成し、式がFalseと評価されたときに指定したオプションの `msg` を適切に返すかどうかをチェックしてください。
def test_my_assert_false():
    assert my_assert(False, "a")=="a"
    assert my_assert(False)=="Assertion!" 
    assert my_assert(True, "a")==False
    assert my_assert(True)==False

# test execution
test_contains()
test_add_name()
test_add_two()
test_divide_by_two()
test_greeting()
test_my_assert_false()