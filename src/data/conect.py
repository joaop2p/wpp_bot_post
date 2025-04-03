from datetime import datetime
from sqlite3 import Cursor, connect
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


class Conection():
    _cursor: Cursor

    def __init__(self) -> None:
        self.con = connect(r"src\data\data.db")
        self._cursor = self.con.cursor()

    def insert(self, processo: int,entregue: bool, tipo: str = None, nome_arquivo: str = None, sit: str = None, numero_usado: int = None, data: datetime = datetime.now()) -> None:
        res = self._cursor.execute(f"SELECT processo from tb_post_sended where processo = {processo}")
        if len(res.fetchall()) < 1:
            self._insert(processo, tipo, nome_arquivo, sit, numero_usado, entregue, data)
        else:
            self._update(processo, tipo, nome_arquivo, sit, numero_usado, entregue, data)

    def _insert(self, processo: int, tipo: str, nome_arquivo: str, sit: str, numero_usado: int, entregue: bool, data: datetime) -> None:
        self._cursor.execute(f"""
            INSERT INTO tb_post_sended (processo, data, tipo, nome_arquivo, sit, numero_usado, entregue)
            VALUES ({processo}, '{data}', '{tipo}', '{nome_arquivo}', '{sit}', {numero_usado}, {entregue})
        """)
        self.con.commit()

    def select(self) -> list[tuple[int, int]]:
        result = self._cursor.execute("select processo, numero_usado from tb_post_sended where entregue = 0")
        return result.fetchall()

    def update_status(self, processo: int, entregue: bool) -> None:
        self._cursor.execute(f"UPDATE tb_post_sended SET entregue = {entregue} WHERE PROCESSO = {processo}")
        self.con.commit()

    def _update(self, processo: int, tipo: str, nome_arquivo: str, sit: str, numero_usado: int, entregue: bool, data: datetime):
        self._cursor.execute(f"""
            UPDATE tb_post_sended
            SET entregue = {entregue}, data = '{data}', tipo = '{tipo}', 
            nome_arquivo = '{nome_arquivo}', sit = '{sit}', numero_usado = {numero_usado}
            WHERE processo = {processo}
        """)
        self.con.commit()

    def kill(self) -> None:
        self.con.close()

if __name__ == "__main__":
    a = Conection()
    # a.insert(processo=202500861, entregue=True, numero_usado=83993838815, data=datetime.strptime("2025-04-01 11:01:57.309016", "%Y-%m-%d %H:%M:%S.%f"), nome_arquivo="Carta Resposta SR 202500861.pdf", tipo='response')
    a.con.commit()
    a.update_status(202500318, False)