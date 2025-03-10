from ..config.db import get_db_connection

class PLC:
    def __init__(self, user_id):
        self.user_id = user_id

    def save(self):
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                # 做正規化表示
                query = "INSERT INTO plc (user_id) VALUES (%s)"

                cursor.execute(query, (
                    self.userid
                ))
            connection.commit()
            return self
        except Exception as e:
            print(f'Error : {e}')
            connection.rollback()
            return None
        finally:
            connection.close()