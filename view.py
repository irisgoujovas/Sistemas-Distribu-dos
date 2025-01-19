#view exibe apenas as informações, sem lógica de código

def show_message(message):
    print(message)

def show_error(message):
    print(f"ERROR: {message}")

#função para exibir o estado 
def show_ticket_status(status):
    if status:
        print(f"Status do bilhete: {status}")
    else:
        print("Bilhete não encontrado.")


