from functions.write_file import write_file

def test(exec1, exec2):
    print(write_file("calculator", exec1, exec2))


test("lorem.txt", "wait, this isn't lorem ipsum")
test("pkg/morelorem.txt", "lorem ipsum dolor sit amet")
test("/tmp/temp.txt", "this should not be allowed")