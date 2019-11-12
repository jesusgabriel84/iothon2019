

### TEST FUNCTION ###
def testit():
    print("this library works.")

#### SOME FUNCTIONS

####### HERE WE CAN HAVE ANOTHER FUNCTION THAT IS USED FOR DECISION making
#### AND IT CAN BE USED WITHIN "on_message" block
def checkroom(room_id,num_of_people):

    #Define room capacity, it can be either calculated or set arbitrarily
    room_1_capacity = 10
    room_2_capacity = 15

    if room_id == 1: ## or tu5, as2 whatever
        if num_of_people == room_1_capacity:
            print("[SMS/MSG sent to USER]: This room is full. Second room will be opened.")

        if num_of_people == 1:
            print("[SMS/MSG sent to USER]:This room will be closed within 10 minutes, please leave the room.")

        if num_of_people != 1 and num_of_people < room_1_capacity:
            if num_of_people > room_1_capacity*0.2 :    ### there are more than 4 people
                print("[SMS/MSG sent to USER]: Room 1 is available. There are {} people inside.".format(num_of_people))
            if num_of_people <= room_1_capacity*0.2 : ### the room is getting less crowded, and soon it can be closed. So send a notification.
                print("[SMS/MSG sent to USER]: Room 1 may be closed soon. There are {} people inside.".format(num_of_people))

    if room_id == 2: ## or tu5, as2 whatever
        if num_of_people == room_2_capacity:
            print("[SMS/MSG sent to USER]: This room is full.")

        if num_of_people == 1:
            print("[SMS/MSG sent to USER]: This room will be closed within 10 minutes, please leave the room.")

        if num_of_people != 1 and num_of_people < room_2_capacity:
            if num_of_people > room_2_capacity*0.2 :    ### there are more than 4 people
                print("[SMS/MSG sent to USER]: Room 2 is available. There are {} people inside.".format(num_of_people))
                
            if num_of_people <= room_2_capacity*0.2 : ### the room is getting less crowded, and soon it can be closed. So send a notification.
                print("[SMS/MSG sent to USER]: Room 2 may be closed soon. There are {} people inside.".format(num_of_people))
