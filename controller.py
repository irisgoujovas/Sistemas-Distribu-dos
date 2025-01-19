from model import create_ticket, get_ticket_status, update_ticket_status
from view import show_message, show_error, show_ticket_status

class TicketController:
    def __init__(self):
        #self.session = Session()
        pass

    def create_new_ticket(self, user_id, event_id, ticket_price, status, category):     
        try:
            # Criar o bilhete com a função no model
            create_ticket(user_id, event_id, ticket_price, status, category)
            show_message("Bilhete criado com sucesso!")
        except Exception as e:
            show_error(f"Erro ao criar o bilhete: {str(e)}")

    #verifica estado do bilhete
    def check_ticket_status(self, ticket_id):
        try:             
            status = get_ticket_status(ticket_id) #recebe o estado do bilhete
            show_ticket_status(status)
        except Exception as e:
            show_error(f"Erro ao buscar o status do bilhete: {str(e)}")

    #método para atualizar o estado do bilhete
    def update_ticket_status_manually(self, ticket_id, new_status):
        try:
            update_ticket_status(ticket_id, new_status) #função dentro do model
            show_message(f"Status do bilhete com ID = {ticket_id}, atualizado para: {new_status}")
        except Exception as e:
            show_error(f"Erro ao atualizar o status do bilhete: {str(e)}")
            
