from functions.get_file_content import get_file_content

def test(dir: str):
    result = get_file_content("calculator", dir)
    if "Error:" in result or dir == "pkg/calculator.py":
        print(result)
    elif dir == "lorem.txt":
        print(f"{dir} length: {len(result)}")
        print(f"{dir} truncated: {'truncated' in result}")
        
    # Para os arquivos menores (main.py e calculator.py), dá print no próprio conteúdo!
    else:
        print("Conteúdo do arquivo:")
        print(result)


test("lorem.txt")
test("main.py")
test("pkg/calculator.py")
test("/bin/cat")
test("pkg/does_not_exist.py")