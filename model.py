import psycopg2 # type: ignore
from psycopg2 import sql # type: ignore

# Conectar ao banco de dados
def connect_db():
    #database_url = os.getenv("DATABASE_URL")
    #return psycopg2.connect(database_url)
    return psycopg2.connect("postgresql://postgres:1234@db/user_db")

# Função para criar um novo usuário
def create_user(user_name, user_email, user_password):
    conn = connect_db()
    cursor = conn.cursor()
    #cursor.execute(
    #    sql.SQL("INSERT INTO user_table (user_name, user_email, user_password) VALUES (%s, %s, %s)"),
    #    (user_name, user_email, user_password)
    #)
    cursor.execute("INSERT INTO user_table (user_name, user_email, user_password) VALUES (%s, %s, %s)", (user_name, user_email, user_password))
    conn.commit()
    cursor.close()
    conn.close()

# Função para buscar um usuário pelo email
def get_user_by_email(user_email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_table WHERE user_email = %s", (user_email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# Função para atualizar a senha de um usuário
def update_user_password(user_email, new_password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE user_table SET user_password = %s WHERE user_email = %s", (new_password, user_email))
    conn.commit()
    cursor.close()
    conn.close()
