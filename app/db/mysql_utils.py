from contextlib import contextmanager

import mysql.connector


class FlaskMysql:
    def __init__(self):
        self.app = None
        self.pool = None

    def get_conn(self):
        if self.pool is None or self.app is None:
            raise Exception('请先初始化数据库')
        return self.pool.get_connection()

    def close_conn(self, conn):
        conn.close()

    @contextmanager
    def with_conn(self):
        try:
            conn = self.get_conn()
            yield conn
        finally:
            self.close_conn(conn)

    def query(self, sql, args=None):
        with self.with_conn() as conn:
            cursor = conn.cursor(prepared=True, dictionary=True)
            cursor.execute(sql, args)
            result = cursor.fetchall()
            cursor.close()
            return result

    def init_db(self):
        config = self.app.config
        host = config['APP_MYSQL_HOST']
        port = config['APP_MYSQL_PORT']
        user = config['APP_MYSQL_USER']
        password = config['APP_MYSQL_PASSWORD']
        database = config['APP_MYSQL_DB']
        pool_size = config['APP_MYSQL_POOL_SIZE']
        self.pool = mysql.connector.pooling.MySQLConnectionPool(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            pool_name='m-pool',
            pool_size=pool_size,
        )

    def init_app(self, app):
        self.app = app
        self.init_db()


db = FlaskMysql()
