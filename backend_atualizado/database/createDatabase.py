import mariadb

conection_database = mariadb.connect(user='root', password='L23092004',host='192.168.1.102', port='2321', database='ExpCriativaapp')
conection_database.close()

conexao = mariadb.Connection(conection_database)#avaliar se vamos usar o sqlite ou mysql
cursor = conexao.cursor()
comando = ''
cursor.execute(comando)
conexao.commit()
resultado = cursor.fetchall()


#create


conexao.close()

