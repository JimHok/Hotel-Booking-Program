if __name__ == '__main__':
    n = int(input())
    room_id = []
    type_name = []
    type_id = []
    date = []
    temp_id = 1
    for i in range(n):
        try:
            a = input().split()
        except EOFError:
            break
        if a[0] == "create":
            b = input().split()
            if b[0] =="book":
                type_name.append([a[2],b[1]])
                type_id.append(b[1])
                room_id.append(temp_id)
                date.append([b[2],b[3]])
                temp_id += 1
            else:
                print("INPUT ERROR!!!!") 
                break 

        elif a[0] == "book":
            type_id.append(a[1])
            room_id.append(temp_id)
            date.append([a[2],a[3]])
            temp_id += 1
        
        elif a[0] == "cancel":
            del type_id[int(a[1])-1]
            del room_id[int(a[1])-1]
            del date[int(a[1])-1]
        
        else:
            print("INPUT ERROR!!!!") 
            break

    # print(type_name)
    # print(type_id)
    # print(room_id)
    # print(date)
        
    for i in range(len(type_name)):
        print("Room:", type_name[i][0])
        for j in range(len(type_id)):
            if type_name[i][1] == type_id[j]:
                print(f"Booking Id {room_id[j]}: {date[j][0]} -> {date[j][1]}")
        print()


# STDIN Input
# 7
# create room Suite
# book 1 5 10
# create room Deluxe
# book 2 1 10
# book 1 12 18
# book 2 20 25
# cancel 4

# STDOUT Output
# Room: Suite
# Booking Id 1: 5 -> 10
# Booking Id 3: 12 -> 18

# Room: Deluxe
# Booking Id 2: 1 -> 10
