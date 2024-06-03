from controller import pengguna as penggunaController 

def loginView() : 
    username = input("Username : ")
    password = input("Password : ")

    try :
        dataPengguna = penggunaController.login(username, password)

        return dataPengguna
    
    except Exception as e :
        print(e)
        loginView()
