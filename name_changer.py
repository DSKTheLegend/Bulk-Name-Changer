import os

want_to_continue = False

dir_list = os.listdir('.')
for file in dir_list : 
    i = 0
    new_name = ''
    ok = ''
    if file != 'name_changer.py':
        org_name = file
        file = file.split(" ")
        index = 0
        for words in file:
            print("[" + str(index) +"] - " + str(words))
            index = index + 1
        anime_index = raw_input("Enter the index position : ")
        anime_name_from = raw_input("Enter the index name starts from : ")
        anime_name_to = raw_input("Enter the index name ends at : ")
        # print(file)
        #   Name Format : <Ep. No> <Anime Name>
        new_name = new_name + ''.join(file[int(anime_index)].split(']')[0]) + ". " + ' '.join(file[int(anime_name_from):int(anime_name_to)+1]) +"."+ ''.join(file[-1].split('.')[-1])
        print(new_name)
        if want_to_continue == False : 
            ok = raw_input("Is the file name ok ? [yes/no] : ")
            if ok == "yes":
                want_to_continue = True
            else:
                print("Exiting . . .")
                exit(1)
        
        #os.rename(org_name,new_name)    