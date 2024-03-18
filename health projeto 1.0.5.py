import mysql.connector
import random
import time

connection = mysql.connector.connect (
     host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'healthdb')

cursor = connection.cursor()

print("Seja bem-vindo ao Take Care by CDGM ")
print("Configurando aguarde...")
comando1 = cursor.execute("CREATE TABLE IF NOT EXISTS PACIENTE(PRONTUARIO VARCHAR(15), CONVENIO VARCHAR(15), NOME VARCHAR(255), IDADE VARCHAR(5), NASCIMENTO VARCHAR(15), CPF VARCHAR(15) ,RG VARCHAR(15), ENDEREÇO VARCHAR(255));")
connection.commit()
comando2 = cursor.execute("CREATE TABLE IF NOT EXISTS FUNCIONÁRIO(MATRICULA VARCHAR(15), NOME VARCHAR(255), IDADE VARCHAR(5), NASCIMENTO VARCHAR(15), ESTADO_CIVIL VARCHAR(15), CPF VARCHAR(15), RG VARCHAR(15), ENDEREÇO VARCHAR(255), CRM_COREN VARCHAR(15), CONTRATO VARCHAR(15), CARGO VARCHAR(255));")
connection.commit()
comando3 = cursor.execute("CREATE TABLE IF NOT EXISTS CONSULTAS(COD_CONSULTA VARCHAR(15), PRONTUARIO VARCHAR(15), NOME VARCHAR(255), IDADE VARCHAR(5), CRM VARCHAR(15), COD_ESPECIALIDADE VARCHAR(5), VALOR_CONSULTA VARCHAR(20), DATA_CONSULTA VARCHAR(15), HORARIO_CONSULTA VARCHAR(15));")
connection.commit()
comando34 = cursor.execute("CREATE TABLE IF NOT EXISTS EXAMES(COD_EXAME VARCHAR(15), PRONTUARIO VARCHAR(15), PACIENTE VARCHAR(255), IDADE VARCHAR(5), TIPO VARCHAR(255), VALOR_EXAME VARCHAR(15), DATA_EXAME VARCHAR(15) , HORARIO_EXAME VARCHAR(15))")
connection.commit()

time.sleep(0.5)

while True:
    menu = int(input("""
    utilize o menu para navegar pelo sistema!
                                      
    1-Pacientes
    2-Funcionários
    3-Agendamentos
    4-Encerrar programa
    Insira a opção escolhida >>:"""))
    
    if menu == 1:
        while True:
            pacientes = int(input("""
    utilize o menu para navegar pelo sistema!
                                  
    1-Cadastrar Pacientes
    2-Atualizar Cadastro
    3-Deletar Cadastro
    4-Visualizar cadastros
    5-Voltar ao menu anterior
    Insira a opção escolhida >>:"""))

            if pacientes == 1:
                while True:
                    print("\nPara cadastrar o paciente é necessario preencher os campos a seguir:")
                    prontuario = random.randint(1000,10000)
                    convenio = input("Digite o número do convênio(este campo pode abrirgar o número do SUS):")
                    nome = input("Digite seu nome aqui:")
                    idade = input("Digite sua idade aqui:")
                    nascimento = input("Digite sua data de nascimento (este campo pode conter '/')")
                    cpf = input("Digite seu cpf aqui:")
                    rg = input("Digite o número do RG:")
                    cep = input("Digite  o CEP:")
                    logadouro = input("Digite o nome do logadouro:")
                    numero = input("Digite o número da residência:")
                    bairro = input("Digite o nome do bairro:")
                    cidade = input("Digite o nome da cidade:")
                    uf = input("Digite UF (apenas siglas): ")
                    endereco = f"{cep}-{logadouro},N-{numero},{bairro},{cidade}-{uf}"
                    comando4 = cursor.execute(f'INSERT INTO PACIENTE VALUES("{prontuario}","{convenio}","{nome}","{idade}","{nascimento}","{cpf}","{rg}","{endereco}")')
                    connection.commit()
                    print("Salvando informações...")
                    time.sleep(1)
                    sair = int(input("Digite 0 caso deseje encerrar o cadastramento de pacientes ou 1 para continuar:"))
                    if sair == 0:
                        break

            elif pacientes == 2:
                while True:
                    print("\nAtenção! as informações serão atualizadas a partir do prontuario do paciente,\ncaso o mesmo esteja duplicado ou com númeração errada é recomendado a exclusão de tais informações.\n")
                    visualizar1 = cursor.execute("Select * From PACIENTE;")
                    resultados = cursor.fetchall()
                    for resultado in resultados:
                        print(resultado)
                    print("\n")
                    
                    atualizar = int(input("""
    Utilize o menu abaixo para navegar e selecione uma opção!
    1-Convenio
    2-Nome
    3-Idade
    4-Nascimento
    5-CPF
    6-RG
    7-Endereço
    8-Voltar ao menu anterior
    Insira a opção escolhida >>: """))
                    
                    print("\nPara atualizar a informação selecionada preencha o campo abaixo!!!")

                    if atualizar == 1:
                        prontuario = input("Digite o número do prontuario:")
                        convenio = input("Digite o número do convênio(este campo pode abrirgar o número do SUS):")
                        comando5 = cursor.execute(f'UPDATE PACIENTE SET  CONVÊNIO = "{convenio}" WHERE PRONTUÁRIO = "{prontuario}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar == 2:
                        prontuario = input("Digite o número do prontuario:")
                        nome = input("Digite seu nome aqui:")
                        comando6 = cursor.execute(f'UPDATE PACIENTE SET  NOME = "{nome}" WHERE PRONTUÁRIO = "{prontuario}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)
                    
                    elif atualizar == 3:
                        prontuario = input("Digite o número do prontuario:")
                        idade = input("Digite sua idade aqui:")
                        comando7 = cursor.execute(f'UPDATE PACIENTE SET  IDADE = "{idade}" WHERE PRONTUÁRIO = "{prontuario}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar == 4:
                        prontuario = input("Digite o número do prontuario:")
                        nascimento = input("Digite sua data de nascimento (este campo pode conter '/')")
                        comando8 = cursor.execute(f'UPDATE PACIENTE SET  NASCIMENTO = "{nascimento}" WHERE PRONTUÁRIO = "{prontuario}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar == 5:
                        prontuario = input("Digite o número do prontuario:")
                        cpf = input("Digite seu cpf aqui:")
                        comando9 = cursor.execute(f'UPDATE PACIENTE SET CPF = "{cpf}" WHERE PRONTUÁRIO = "{prontuario}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar == 6:
                        prontuario = input("Digite o número do prontuario:")
                        rg = input("Digite o número do RG:")
                        comando10 = cursor.execute(f'UPDATE PACIENTE SET  RG = "{rg}" WHERE PRONTUÁRIO = "{prontuario}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)
 
                    elif atualizar == 7:
                        prontuario = input("Digite o número do prontuario:")
                        cep = input("Digite  o CEP:")
                        logadouro = input("Digite o nome do logadouro:")
                        numero = input("Digite o número da residência:")
                        bairro = input("Digite o nome do bairro:")
                        cidade = input("Digite o nome da cidade:")
                        uf = input("Digite UF (apenas siglas): ")
                        endereco = f"{cep}-{logadouro},N-{numero},{bairro},{cidade}-{uf}"
                        comando11 = cursor.execute(f'UPDATE PACIENTE SET  ENDERECO = "{endereco}" WHERE PRONTUÁRIO = "{prontuario}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    else:
                        break

            elif pacientes == 3:
                delete = cursor.execute("Select * from PACIENTE;")
                resultados = cursor.fetchall()
                for resultado in resultados:
                    print(*resultado, sep=" - ")
                print("\nPreencha o campo abaixo para excluir um paciente!")
                prontuario = input("\nDigite o número do prontuario:")
                comando12 = cursor.execute(f'DELETE  FROM PACIENTE WHERE PRONTUÁRIO = "{prontuario}";')
                connection.commit()
                time.sleep(0.5)
                print("Deletando informações...")
                
            
            elif pacientes == 4:
                print("\nCarrengando Informações...\n")
                time.sleep(1)
                visualizar2 = cursor.execute("Select * From PACIENTE;")
                resultados = cursor.fetchall()
                for resultado in resultados:
                    print(*resultado, sep=" - ")
               

            else:
                break

    elif menu == 2:
        while True:
            funcionarios = int(input("""
            1-Cadastar Funcioário
            2-Atualizar Cadastro
            3-Deletar Cadastro
            4-Visualizar Cadastro
            5-Voltar ao menu anterior
           Insira a opção escolhida >>:"""))

            if funcionarios == 1:
                while True:
                    print("\nPreencha os campos a seguir para realizar o cadastro de funcionários: ")
                    matricula = random.randint(15000,25000 )
                    nome_funcionario = input("Digite o nome:")
                    idade_funcionario = input("Digite a idade:")
                    nascimento_funcionario = input("Digite a Data de Nascimento (este campo pode conter caracteres como /):")
                    estado_civil = input("Digite o Estado Civil:")
                    cpf_funcionario = input("Digite o CPF(digite somente números):")
                    rg_funcionario = str(input("Digite o RG:"))
                    cep_funcionario = input("Digite  o CEP:")
                    logadouro_funcionario = input("Digite o nome do logadouro:")
                    numero_funcionario = input("Digite o número da residência:")
                    bairro_funcionario = input("Digite o nome do bairro:")
                    cidade_funcionario = input("Digite o nome da cidade:")
                    uf_funcionario = input("Digite UF (apenas siglas): ")
                    endereco_funcionario = f"{cep_funcionario}-{logadouro_funcionario},N-{numero_funcionario},{bairro_funcionario},{cidade_funcionario}-{uf_funcionario}"
                    crm_coren = input("Digite a númeração do CRM ou COREN (caso o mesmo não tenha insira --):")
                    contrato = random.randint(30000,40000)
                    cargo = input("Digite o Cargo que será ocupado:")
                    comando13 = cursor.execute (f'INSERT INTO FUNCIONÁRIO VALUES("{matricula}","{nome_funcionario}","{idade_funcionario}","{nascimento_funcionario}","{estado_civil}","{cpf_funcionario}","{rg_funcionario}","{endereco_funcionario}","{crm_coren}","{contrato}","{cargo}")')
                    connection.commit()
                    print("Salvando informações...")
                    time.sleep(1)
                    sair = int(input("Digite 0 caso deseje encerrar o cadastramento ou 1 para continuar:"))

                    if sair == 0: 
                        break

            elif funcionarios == 2:
                while True:

                    print("\nAtenção! as informações serão atualizadas a partir da matrícula do funcionário,\ncaso a mesma esteja duplicado ou com númeração errada é recomendado a exclusão de tais informações.\n")
                    visualizar3= cursor.execute("Select * From FUNCIONÁRIO;")
                    resultados = cursor.fetchall()
                    for resultado in resultados:
                        print(*resultado, sep=" - ")
                    print("\n")

                    atualizar_fun = int(input("""
    1-Nome
    2-Idade
    3-Nascimento
    4-Estado Civil
    5-CPF
    6-RG
    7-Endereço
    8-CRM/COREN
    9-Cargo
    0-Voltar ao menu anterior
    Insira a opção escolhida >>:"""))
                    if atualizar_fun ==1:
                        matricula = input("Digite o número da matricula:")
                        nome_funcionario = input("Digite o nome:")
                        comando14 = cursor.execute(f'UPDATE FUNCIONÁRIO SET NOME = "{nome_funcionario}" WHERE MATRICULA = "{matricula}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar_fun == 2:
                        matricula = input("Digite o número da matricula:")
                        idade_funcionario = input("Digite a idade:")
                        comando15 = cursor.execute(f'UPDATE FUNCIONÁRIO SET IDADE = "{idade_funcionario}" WHERE MATRICULA = "{matricula}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar_fun == 3:
                        matricula = input("Digite o número da matricula:")
                        nascimento_funcionario = input("Digite a Data de Nascimento (este campo pode conter caracteres como /):")
                        comando16 = cursor.execute(f'UPDATE FUNCIONÁRIO SET NASCIMENTO = "{nascimento_funcionario}" WHERE MATRICULA = "{matricula}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar_fun == 4:
                        matricula = input("Digite o número da matricula:")
                        estado_civil = input("Digite o Estado Civil:")
                        comando17 = cursor.execute(f'UPDATE FUNCIONÁRIO SET ESTADO_CIVIL = "{estado_civil}" WHERE MATRICULA = "{matricula}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar_fun == 5:
                        matricula = input("Digite o número da matricula:")
                        cpf_funcionario = input("Digite o CPF(digite somente números):")
                        comando18 = cursor.execute(f'UPDATE FUNCIONÁRIO SET CPF = "{cpf_funcionario}" WHERE MATRICULA = "{matricula}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar_fun == 6:
                        matricula = input("Digite o número da matricula:")
                        rg_funcionario = str(input("Digite o RG:"))
                        comando19 = cursor.execute(f'UPDATE FUNCIONÁRIO SET RG = "{rg_funcionario}" WHERE MATRICULA = "{matricula}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar_fun == 7:
                        matricula = input("Digite o número da matricula:")
                        cep = input("Digite  o CEP:")
                        logadouro = input("Digite o nome do logadouro:")
                        numero = input("Digite o número da residência:")
                        bairro = input("Digite o nome do bairro:")
                        cidade = input("Digite o nome da cidade:")
                        uf = input("Digite UF (apenas siglas): ")
                        endereco_funcionario = f"{cep}-{logadouro},N-{numero},{bairro},{cidade}-{uf}"
                        comando20 = cursor.execute(f'UPDATE FUNCIONÁRIO SET ENDEREÇO = "{endereco_funcionario}" WHERE MATRICULA = "{matricula}" ')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar_fun == 8:
                        matricula = input("Digite o número da matricula:")
                        crm_coren = input("Digite a númeração do CRM ou COREN (caso o mesmo não tenha insira --):")
                        comando21 = cursor.execute(f'UPDATE FUNCIONÁRIO SET CRM_OU_COREN = "{crm_coren}" WHERE MATRICULA = "{matricula}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

                    elif atualizar_fun == 9:
                        matricula = input("Digite o número da matricula:")
                        cargo = input("Digite o Cargo que será ocupado:")
                        comando22 = cursor.execute(f'UPDATE FUNCIONÁRIO SET CARGO = "{cargo}" WHERE MATRICULA = "{matricula}"')
                        connection.commit()
                        print("Atualizando informações...")
                        time.sleep(1)

 
                    else:
                        break


            elif funcionarios == 3:
                delete1 = cursor.execute("Select * from FUNCIONÁRIO;")
                resultados = cursor.fetchall()
                for resultado in resultados:
                    print(*resultado, sep=" - ")

                print("\nPreencha o campo abaixo para excluir um paciente!")
                matricula = input("\nDigite o número da matrícula:")
                comando23 = cursor.execute(f'DELETE FROM FUNCIONÁRIO WHERE MATRICULA = "{matricula}";')
                connection.commit()
                time.sleep(0.5)
                print("Deletando informações...")

            elif funcionarios == 4:
                print("Consultando o banco de dados aguarde...")
                time.sleep(0.5)
                visualizar4 = cursor.execute("Select * from FUNCIONÁRIO;")
                resultados = cursor.fetchall()
                for resultado in resultados:
                    print(*resultado, sep=" - ")

            else:
                break
    elif menu == 3:
        while True:
            agendamentos = int(input("""
    1-Agendamentos de Consultas
    2-Agendamentos de Exames
    3-Voltar ao menu anterior
    Insira a opção escolhida >>:""")) 
            
            if agendamentos == 1:
                while True:

                    consultas = int(input("""
    1-Agendar Consultas
    2-Atualizar Consultas
    3-Delete Consultas
    4-Visualizar Consultas
    5-Voltar ao menu anterior
    insira a opção escolhida >>:"""))
                
                    if consultas == 1:
                        while True:
                            print('\npreencha os campos abaixos para agendar uma consulta:')
                            print("""\nEspecialidades:
    001-Clinico Geral
    002-Cardiologista
    003-Neurologista
    004-Oftalmologista
    005-Otorrinoaringologista
    006-Endocrinolista
    """)
                            cod_consultas = random.randint(100,999)
                            prontuario = input("\nInsira o prontuário do paciente:")
                            nome_consulta = input("Insira o nome do paciente:")
                            idade_consulta = input("insira a idade do paciente:")
                            crm = input("Insira o CRM do médico responsável:")
                            cod_especialidade = input("Insira  o código da especialidade:") 
                            valor_consulta = input("insira o valor da consulta:")
                            horario_consulta = input("insira o horário que será realizada a consulta:")
                            data_consulta = input("Insira a data que será realizada consulta:")
                            comando24 = cursor.execute (f'INSERT INTO  CONSULTAS VALUES("{cod_consultas}","{prontuario}","{nome_consulta}","{idade_consulta}","{crm}","{cod_especialidade}","{valor_consulta}","{horario_consulta}","{data_consulta}")')
                            connection.commit()
                            sair = int(input("Digite 0 caso deseje encerrar o cadastramento ou 1 para continuar:"))

                            if sair == 0: 
                                break

                    elif consultas == 2:
                        while True:
                            print("\nAtenção! As consultas serão atualizadas apartir do código de consutas!!!\n")
                            visualizar5 = cursor.execute("Select * from CONSULTAS;")
                            resultados = cursor.fetchall()
                            for resultado in resultados:
                                print(*resultado, sep=" - ")

                            atualizar_consultas = int(input("""
    1-Prontuario
    2-Nome
    3-Idade
    4-CRM
    5-Código especialidade
    6-Valor
    7-Horário
    8-Data
    9-voltar ao menu anterior 
    insira a opção escolhida >>:"""))
                            
                            if atualizar_consultas == 1:
                                cod_consultas = input("\nInsira o código da consulta: ")
                                prontuario = input("Insira o prontuário:")
                                comando25 = cursor.execute(f'UPDATE CONSULTAS SET PRONTUARIO = "{prontuario}" WHERE COD_CONSULTA = "{cod_consultas}" ')
                                connection.commit()
                                print("Atualizando informações...")
                                time.sleep(1)

                            elif atualizar_consultas == 2:
                                cod_consultas = input("\nInsira o código da consulta:")
                                nome_consulta = input("Insira o nome do paciente:")
                                comando26 = cursor.execute(f'UPDATE CONSULTAS SET NOME = "{nome_consulta}" WHERE COD_CONSULTA = "{cod_consultas}" ')
                                connection.commit()

                            elif atualizar_consultas == 3:
                                cod_consultas = input("\nInsira o código da consulta:")
                                idade_consulta = input("Insira a idade do paciente:")
                                comando27 = cursor.execute(f'UPDATE CONSULTAS SET IDADE = "{idade_consulta}" WHERE COD_CONSULTA = "{cod_consultas}"')
                                connection.commit()

                            elif atualizar_consultas == 4:
                                cod_consultas = input("\nInsira o código da consulta:")
                                crm = input("insira o CRM do médico responsável:")
                                comando28 = cursor.execute(f'UPDATE CONSULTAS SET CRM = "{crm}" WHERE COD_CONSULTA = "{cod_consultas}" ')
                                connection.commit()
                                print("Atualizando informações...")
                                time.sleep(1)

                            elif atualizar_consultas == 5:
                                cod_consultas = input("\nInsira o código da consulta:")
                                cod_especialidade = input("insira o código da especialidade:")
                                comando29 = cursor.execute(f'UPDATE CONSULTAS SET COD_ESPECIALIDADE = "{cod_especialidade}" WHERE COD_CONSULTA = "{cod_consultas}" ')
                                connection.commit()
                                print("Atualizando informações...")
                                time.sleep(1)
                            
                            elif atualizar_consultas == 6:
                                cod_consultas = input("\nInsira o código de consultas:")
                                valor_consulta = input("Insira o valor:")
                                comando30 = cursor.execute(f'UPDATE CONSULTAS SET VALOR_CONSULTA = "{valor_consulta}" WHERE COD_CONSULTA = "{cod_consultas}" ')
                                connection.commit()
                                print("Atualizando informações...")
                                time.sleep(1)

                            elif atualizar_consultas == 7:
                                cod_consultas = input("\nInsira o código da consulta:")
                                horario_consulta = input("Insira o hórario da consulta:")
                                comando31 = cursor.execute(f'UPDATE CONSULTAS SET HORARIO_CONSULTA = "{horario_consulta}" WHERE COD_CONSULTA = "{cod_consultas}"')
                                connection.commit()
                                print("Atualizando informações...")
                                time.sleep(1)

                            elif atualizar_consultas == 8:
                                cod_consultas = input("\nInsira o código da consulta:")
                                data_consulta = input("Insira a data da consulta (este campo pode abrigar '/')")
                                comando32 = cursor.execute(f'UPDATE CONSULTAS SET DATA_CONSULTA = "{data_consulta}" WHERE COD_CONSULTA = "{cod_consultas}"')
                                connection.commit()
                                print("Atualizando informações...")
                                time.sleep(1)

                            else:
                                break

                    elif consultas == 3:
                        print("\nPreencha o campo abaixo para excluir uma consulta!!!")
                        print("Consultando o banco de dados aguarde...")
                        time.sleep(1)

                        visualizar6 = cursor.execute("Select * from CONSULTAS;")
                        resultados = cursor.fetchall()
                        for resultado in resultados:
                            print(*resultado, sep=" - ")

                        cod_consultas = input("Insira o código da consulta:")
                        comando33 = cursor.execute(f'DELETE FROM CONSULTAS WHERE COD_CONSULTA = "{cod_consultas}" ')
                        connection.commit()
                        

                    
                    elif consultas == 4:
                        print("\nConsultando o banco de dados aguarde...")
                        time.sleep(1)
                        visualizar7 = cursor.execute("Select * From CONSULTAS;")
                        resultados = cursor.fetchall()
                        for resultado in resultados:
                            print(*resultado, sep=" - ")
                    
                    else:
                        break

            elif agendamentos == 2: 
                while True:

                    exames = int(input("""
    1-Agendar exame
    2-Atualizar exame
    3-Deletar exame
    4-Visualizar exame
    5-Voltar ao menu anterior
    insira a opção escolhida >>: """))
                    
                    if exames == 1:
                        while True:
                            cod_exame = random.randint(100, 999)
                            prontuario_exame = input("\nInsira o prontuário do paciente:")
                            paciente_exame = input("Insira o nome do paciente:")
                            idade_exame = input("Insira a idade do paciente:")
                            tipo_exame = input("Insira o tipo de exame:")
                            valor_exame = input("Insira o  valor do exame:")
                            data_exame = input("Insira a data do exame:")
                            horario_exame = input("Insira o horário do exame:")
                            comando35 = cursor.execute(f'INSERT INTO EXAMES VALUES("{cod_exame}", "{prontuario_exame}", "{paciente_exame}", "{idade_exame}", "{tipo_exame}", "{valor_exame}", "{data_exame}", "{horario_exame}")')
                            connection.commit()
                            print("Salvando informações...")
                            time.sleep(1)
                            sair = int(input("Digite 0 caso deseje encerrar o cadastramento ou 1 para continuar:"))

                            if sair == 0:
                                break

                    
                    elif exames == 2:
                        while True:
                            print("")
                            visualizar1 = cursor.execute("Select * From EXAMES;")
                            resultados = cursor.fetchall()
                            for resultado in resultados:
                                print(*resultado, sep=" - ")
                            print("\n")
                            atualizar_exame = int(input("""
    1-Prontuário
    2-Paciente
    3-Idade
    4-Tipo
    5-Valor
    6-Data
    7-horario
    8-Voltar ao menu anterior
    insira a opção escolhida >>:"""))
                            
                            if atualizar_exame == 1:
                                cod_exame = input("\nInsira o código de exames:")
                                prontuario_exame = input("Insira o prontuário do paciente:")
                                comado36 = cursor.execute(f'UPDATE EXAMES SET PRONTUARIO = "{prontuario_exame}" WHERE COD_EXAME = "{cod_exame}"')
                                connection.commit()

                            elif atualizar_exame == 2:
                                cod_exame = input("\nInsira o código do exame:")
                                paciente_exame = input("Insira o nome do paciente:")
                                comando37 = cursor.execute(f'UPDATE EXAMES SET PACIENTE = "{paciente_exame}" WHERE COD_EXAME = "{cod_exame}"')
                                connection.commit()
                            
                            elif atualizar_exame == 3:
                                cod_exame = input("\nInsira o código do exame:")
                                idade_exame = input("Insira a idade do paciente:")
                                comado38 = cursor.execute(f'UPDATE EXAMES SET IDADE = "{idade_exame}" WHERE COD_EXAME = "{cod_exame}"')
                                connection.commit()

                            elif atualizar_exame == 4:
                                cod_exame = input("\nInsira o código do exame:")
                                tipo_exame = input("Insira o tipo de exame:")
                                comando39 = cursor.execute(f'UPDATE EXAMES SET TIPO = "{tipo_exame}" WHERE COD_EXAME = "{cod_exame}"')
                                connection.commit()

                            elif atualizar_exame == 5:
                                cod_exame = input("\nInsira o código do exame:")
                                valor_exame = input("Insira o valor do exame:")
                                comando40 = cursor.execute(f'UPDATE EXAMES SET VALOR_EXAME = "{valor_exame}" WHERE COD_EXAME = "{cod_exame}"')
                                connection.commit()
                            
                            elif atualizar_exame == 6:
                                cod_exame = input("\nInisra o código do exame:")
                                data_exame = input("Insira a data do exame:")
                                comado41 = cursor.execute(f'UPDATE EXAMES SET DATA_EXAME = "{data_exame}" WHERE COD_EXAME = "{cod_exame}"')
                            
                            elif atualizar_exame == 7:
                                cod_exame = input("\nInsira o código do exame:")
                                horario_exame = input("Insira o horário do exame:")
                                comando42 = cursor.execute(f'UPDATE EXAMES SET HORARIO_EXAME = "{horario_exame}" WHERE COD_EXAME = "{cod_exame}"')
                                connection.commit()



                            else:
                                break

                    elif exames == 3:
                        print("\nPreencha o campo abaixo para excluir um exame!")
                        print("Consultando o banco de dados aguarde...\n")
                        time.sleep(1)

                        visualizar6 = cursor.execute("Select * from EXAMES;")
                        resultados = cursor.fetchall()
                        for resultado in resultados:
                            print(*resultado, sep=" - ")

                        cod_exame = input("\nInsira o código do exame:")
                        comando43 = cursor.execute(f'DELETE FROM EXAMES WHERE COD_EXAME = "{cod_exame}" ')
                        connection.commit()

                    elif exames == 4:
                        print("\nConsultando o banco de dados aguarde...\n")
                        time.sleep(1)

                        visualizar7 = cursor.execute("Select * from EXAMES;")
                        resultados = cursor.fetchall()
                        for resultado in resultados:
                            print(*resultado, sep=" - ")

                    
                    else:
                        break

                    
            else:
                break


    else:
        break
connection.close()