import database

def create_users_table():
    connection = database.get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

# def create_posts_table():
#     connection = database.get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS posts (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             title VARCHAR(255) NOT NULL,
#             content TEXT NOT NULL,
#             author_id INT NOT NULL,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#             updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#             FOREIGN KEY (author_id) REFERENCES users(id)
#         )
#     """)
#     connection.commit()
#     cursor.close()
#     connection.close()