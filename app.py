from controller import TicketController
from view import show_message, show_error
from model import get_event_title

def menu():
    controller = TicketController()

    while True:
        #Exibe o menu de opções para o usuário
        print("""\nEscolha uma opção:
        1. Adicionar bilhete
        2. Verificar estado do bilhete
        3. Atualizar estado do bilhete
        4. Sair""")
        
        #Pede uma opção ao usuário
        choice = input("Opção: ")
        
        #Opção 1: Adicionar bilhete
        if choice == "1":
            try:
                user_id = input("Digite o ID do usuário: ")
                event_id = input("Digite o ID do evento: ")

                # Chama a função para obter o nome do evento
                event_name = get_event_title(event_id)

                if event_name:
                    print(f"Bilhete para o evento: {event_name}")
                else:
                    print("Evento não encontrado.")

                ticket_price = input("Digite o preço do bilhete: ")
                status = "Não confirmado" #estado default
                category = input("Digite a categoria do bilhete(VIP, normal): ")

                #Verifica se os valores são válidos
                if not user_id.isdigit() or not event_id.isdigit() or not ticket_price.replace(".", "", 1).isdigit():
                    raise ValueError("ID e preço devem ser números válidos.")
                
                controller.create_new_ticket(user_id, event_id, ticket_price, status, category) #chama o método no controller para criar o bilhete
            
            except ValueError as ve:
                show_error(str(ve))
            except Exception as e:
                show_error(f"Erro ao criar bilhete: {str(e)}")

        #Opção 2: Verificar estado do bilhete
        elif choice == "2":
            try:
                ticket_id = input("Digite o ID do bilhete: ")
                if not ticket_id.isdigit():
                    raise ValueError("O ID do bilhete deve ser um número inteiro.")
                
                #chama controller para verificar o estado do bilhete
                controller.check_ticket_status(ticket_id)
            
            except ValueError as ve:
                show_error(str(ve))
            except Exception as e:
                show_error(f"Erro ao buscar status do bilhete: {str(e)}")

        #Opçãp 3: Atualizar estado do bilhete
        elif choice == "3": 
            try:
                ticket_id = input("Digite o ID do bilhete: ")
                if not ticket_id.isdigit():
                    raise ValueError("O ID do bilhete deve ser um número inteiro.")
                
                #recebe o novo estado do bilhete
                new_status = input("Digite o novo status do bilhete (ex: 'confirmado', 'cancelado'): ").strip().lower()
                if new_status not in ["confirmado", "cancelado", "não confirmado"]:
                    raise ValueError("Status inválido. Use: 'confirmado', 'cancelado', ou 'não confirmado'.")
                
                #atualiza o novo estado do bilhete
                controller.update_ticket_status_manually(ticket_id, new_status)
            
            except ValueError as ve:
                show_error(str(ve))
            except Exception as e:
                show_error(f"Erro ao atualizar status do bilhete: {str(e)}")

        #Opção 4: Sair
        elif choice == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
