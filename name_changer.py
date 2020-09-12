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
        # print(file)
        #   Name Format : <Ep. No> <Anime Name>
        new_name = new_name + ''.join(file[9].split(']')[0]) + ". " + ' '.join(file[1:8]) +"."+ ''.join(file[-1].split('.')[-1])
        print(new_name)
        if want_to_continue == False : 
            ok = raw_input("Is the file name ok ? [yes/no] : ")
            if ok == "yes":
                want_to_continue = True
            else:
                print("Exiting . . .")
                os.exit(1)
        
        os.rename(org_name,new_name)    