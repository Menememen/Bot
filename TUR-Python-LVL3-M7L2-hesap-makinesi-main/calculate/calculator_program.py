def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Sıfıra bölme hatası!")
    else:
        raise ValueError("Bilinmeyen işlem!")


def main():
    print("Basit Hesap Makinesi. İki sayı girin ve bir işlem seçin.")
    try:
        num1 = float(input("İlk sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))
        operation = input("Bir işlem seçin (+, -, *, /): ")
        result = calculate(num1, num2, operation)
        print(f"Sonuç: {result}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()