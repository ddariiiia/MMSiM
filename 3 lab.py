def check_line(line):
    spaces = line.count(' ')
    if spaces == 4:
        result = 'ДА '
    else:
        result = 'НЕТ'
    return result

if __name__ == "__main__":
    text_file = open('C://Users//daria//OneDrive//Рабочий стол//10 семестр//Мат медоды сокрытия и маскирования информации//3//text.txt', 'r', encoding='UTF-8')
    for line in text_file:
        print(line, end='')
    text_file.close()
    print('----------------------------------------')
    text_file = open('C://Users//daria//OneDrive//Рабочий стол//10 семестр//Мат медоды сокрытия и маскирования информации//3//text.txt', 'r', encoding='UTF-8')
    with open('C://Users//daria//OneDrive//Рабочий стол//10 семестр//Мат медоды сокрытия и маскирования информации//3//textend.txt', 'w', encoding='UTF-8') as textend_file:
        for line in text_file:
            result = check_line(line)
            print(result, '|', line, end='')
            if result.strip() == 'ДА':
                textend_file.write(line)
    text_file.close()