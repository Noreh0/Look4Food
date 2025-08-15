import mariadb

conection_database = mariadb.connect(user='root', password='senha',host='ip', port='port', database='ExpCriativaapp')
conection_database.close()

conexao = mariadb.Connection(conection_database)#avaliar se vamos usar o sqlite ou mysql
cursor = conexao.cursor()
comando = ''
cursor.execute(comando)
conexao.commit()
resultado = cursor.fetchall()


#create


conexao.close()


