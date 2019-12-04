import os

from mysql.connector import Error

from connection_pool.coneection_pool_study02 import ExplicitlyConnectionPool


class BackupRestore:
    OPTION = """
        CHARACTER SET 'UTF8'
        FIELDS TERMINATED by ','
        LINES TERMINATED by '\r\n'
        """

    def __init__(self, source_dir='/tmp/', data_dir='/tmp/'):
        self.source_dir = source_dir
        self.data_dir = data_dir

    def data_backup(self, table_name):
        filename = table_name + '.txt'
        try:
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()

            source_path = self.source_dir + filename  # /tmp/product.txt
            # if os.path.exists(source_path):
            #     os.remove(source_path)

            backup_sql = "SELECT * FROM {} INTO OUTFILE '{}' {}".format(table_name, source_path, BackupRestore.OPTION)
            cursor.execute(backup_sql)

            # if not os.path.exists(self.data_dir):
            #     os.makedirs(os.path.join('data'))
            # shutil.move(source_path, self.data_dir + '/' + filename)  # 파일이 존재하면 overwrite
            # shutil.copy(source_path, self.data_dir + '/' + filename)
            print(table_name, "backup complete!")
        except Error as err:
            print(err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def data_restore(self, table_name):
        filename = table_name + '.txt'
        try:
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            # source_path = self.source_dir + filename  # /tmp/product.txt
            # if os.path.exists(source_path):
            #     os.remove(source_path)
            data_path = os.path.abspath(self.data_dir + filename).replace('\\', '/')
            restore_sql = "LOAD DATA INFILE '{}' INTO TABLE {} {}".format(data_path, table_name,
                                                                                BackupRestore.OPTION)
            cursor.execute(restore_sql)
            conn.commit()
            # if not os.path.exists(self.data_dir):
            #     os.makedirs(os.path.join('data'))
            # shutil.move(source_path, self.data_dir + '/' + filename)  # 파일이 존재하면 overwrite
            # shutil.copy(source_path, self.data_dir + '/' + filename)
            print(table_name, "restore complete!")
        except Error as err:
            print(err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
