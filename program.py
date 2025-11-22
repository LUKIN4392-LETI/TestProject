def gray_code(n):
    if n == 0:
        return ['']
    
    # Рекурсивно получаем коды Грея для n-1
    prev = gray_code(n - 1)
    
    # Создаем новую последовательность:
    # сначала добавляем '0' к каждому коду из предыдущей последовательности,
    # затем добавляем '1' к каждому коду из reversed(предыдущей последовательности)
    return ['0' + code for code in prev] + ['1' + code for code in reversed(prev)]

def main():
    n = int(input().strip())
    codes = gray_code(n)
    
    for code in codes:
        print(code)

if __name__ == "__main__":
    main()