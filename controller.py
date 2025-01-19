from model import create_user, get_user_by_email, update_user_password
from view import show_message, show_error

def register_user(user_name, user_email, user_password):
    # Verificar se o usuário já existe
    existing_user = get_user_by_email(user_email)
    if existing_user:
        show_error("O usuário com este e-mail já existe.")
        return
    
    # Criar o usuário
    create_user(user_name, user_email, user_password)
    show_message(f"Usuário {user_name} registrado com sucesso!")

def login_user(user_email, user_password):
    user = get_user_by_email(user_email)
    if not user:
        show_error("Usuário não encontrado.")
        return
    elif user[3] != user_password:  # user[3] é a senha da base de dados
        show_error("Senha incorreta.")
        return
    else:
        show_message(f"Bem-vindo, {user[1]}!")  # user[1] é o nome do usuário

def change_password(user_email, new_password):
    user = get_user_by_email(user_email)
    if not user:
        show_error("Usuário não encontrado.")
        return
    update_user_password(user_email, new_password)
    show_message("Senha atualizada com sucesso!")
