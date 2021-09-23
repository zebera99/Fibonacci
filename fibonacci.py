previous_num = 0
current_num = 1
count = 1


while count <= 50:
    print(current_num)
    save_num = previous_num
    previous_num = current_num
    current_num = current_num + save_num

    count += 1
