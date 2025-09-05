import sqlite3

banco= sqlite3.connect('hospital.db')

cursor= banco.cursor()

# # 1) Selecionar todos os pacientes da cidade de São Paulo .
cursor.execute("SELECT nome FROM pacientes WHERE cidade = 'São Paulo'")
print(cursor.fetchall())

# # 2) Listar o nome e diagnóstico dos pacientes com idade acima de 40 anos .
cursor.execute("SELECT nome, diagnostico FROM pacientes WHERE idade > 40")
print(cursor.fetchall())

# # 3) Mostrar o nome e plano de saúde dos pacientes atendidos pelo plano Unimed .
cursor.execute("SELECT nome, plano_saude FROM pacientes WHERE plano_saude = 'Unimad' ")
print(cursor.fetchall())

# # 4) Selecionar os pacientes ordenados pelos dados de internação (mais antigo primeiro) .
cursor.execute("SELECT nome, data_internacao FROM pacientes ORDER BY data_internacao ASC")
print(cursor.fetchall())

# # 5) Mostrar apenas os pacientes que tiveram diagnóstico de Fratura .
cursor.execute("SELECT nome, diagnostico FROM pacientes WHERE diagnostico = 'Fratura'")
print(cursor.fetchall())

# 6) Selecionar os pacientes que foram atendidos pelo Dr João.
cursor.execute("SELECT nome, medico_responsavel FROM pacientes WHERE medico_responsavel = 'Dr. João'")
print(cursor.fetchall())