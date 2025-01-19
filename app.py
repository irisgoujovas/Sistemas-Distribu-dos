from controller import register_user, login_user, change_password

if __name__ == "__main__":
#def menu():
    while True:
        print("""\nEscolha uma opção:
        1. Registrar Usuário
        2. Fazer Login
        3. Alterar Senha
        4. Sair""")
        
        choice = input("Opção: ")
        
        if choice == "1":
            user_name = input("Nome do usuário: ")
            user_email = input("Email do usuário: ")
            user_password = input("Senha do usuário: ")
            register_user(user_name, user_email, user_password)

        elif choice == "2":
            user_email = input("Email: ")
            user_password = input("Senha: ")
            login_user(user_email, user_password)

        elif choice == "3":
            user_email = input("Email: ")
            new_password = input("Nova senha: ")
            change_password(user_email, new_password)

        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#if __name__ == "__main__":
#    menu()
