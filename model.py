import psycopg2 #type: ignore
from psycopg2 import sql #type: ignore

# Conectar ao banco de dados
def connect_db():
    return psycopg2.connect("postgresql://postgres:1234@db/ticket_db")

# Função para criar um bilhete
def create_ticket(user_id, event_id, ticket_price, status, category):
    conn = connect_db()
    cursor = conn.cursor()
    #Inserir novo bilhete
    cursor.execute(
        sql.SQL("INSERT INTO ticket_table (user_id, event_id, ticket_price, status, category) VALUES (%s, %s, %s, %s, %s)"),
        (user_id, event_id, ticket_price, status, category)
    )
    conn.commit() #confirma a transação
    cursor.close()
    conn.close()

# Função para obter o estado de um bilhete
def get_ticket_status(ticket_id):
    conn = connect_db()
    cursor = conn.cursor()
    #vai buscar o estado do bilhete
    cursor.execute("SELECT status FROM ticket_table WHERE ticket_id = %s", (ticket_id))
    status = cursor.fetchone() #recupera o resultado
    cursor.close()
    conn.close()
    
    if status:
        return status[0]  # Acessa o primeiro elemento da tupla, que é o status
    else:
        return None

# Função para atualizar o status do bilhete
def update_ticket_status(ticket_id, new_status):
    conn = connect_db()
    cursor = conn.cursor()
    #Atualiza o estado
    cursor.execute(
        "UPDATE ticket_table SET status = %s WHERE ticket_id = %s",
        (new_status, ticket_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_event_title(event_id):
    try:
        # Conectar ao banco de dados do microserviço de eventos
        conn = psycopg2.connect("dbname=event_db user=postgres password=1234 host=db")
        cursor = conn.cursor()

        # Executar consulta para pegar o nome do evento
        cursor.execute("SELECT event_name FROM event_table WHERE event_id = %s", (event_id,))
        event = cursor.fetchone()

        # Fechar a conexão
        cursor.close()
        conn.close()

        if event:
            return event[0]  # Retorna o nome do evento
        else:
            return None #retorna none se o evento não for encontrado
    except Exception as e:
        return f"Erro ao buscar evento: {str(e)}"

