CREATE TABLE Cargo (
	Id_Cargo INT PRIMARY KEY,
	Tipo_Cargo VARCHAR NOT NULL,
	Nome_cargo VARCHAR NOT NULL,
	Salario float NOT NULL,
	Descricao VARCHAR NOT NULL,
	Horario VARCHAR NOT NULL
);

CREATE TABLE Convenio (
	Id_Convenio INT PRIMARY KEY NOT NULL,
	Nome_convenio VARCHAR NOT NULL,
	CNPJ VARCHAR NOT NULL
);

CREATE TABLE Plano_convenio (
	Id_Plano INT PRIMARY KEY NOT NULL,
	Nome_Plano VARCHAR NOT NULL,
	Id_Convenio INT NOT NULL,
	FOREIGN KEY (Id_Convenio) REFERENCES Convenio(Id_Convenio)
);

CREATE TABLE Prescricao (
	Id_Prescricao INT PRIMARY KEY NOT NULL,
	Exame VARCHAR NOT NULL,
	Medicamento VARCHAR NOT NULL,
	Tratamento VARCHAR NOT NULL,
	Descricao_consultas VARCHAR NOT NULL
);

CREATE TABLE Especialidade (
	Id_Especialidade INT PRIMARY KEY,
	Tipo_Especialidade VARCHAR NOT NULL
);

CREATE TABLE Funcionario (
	Id_Funcionario INT PRIMARY KEY NOT NULL,
	Nome VARCHAR NOT NULL,
	Sobrenome VARCHAR NOT NULL,
	Genero VARCHAR,
	CPF VARCHAR NOT NULL,
	Data_Nascimento date NOT NULL,
	Telefone VARCHAR,
	Celular VARCHAR,
	Email VARCHAR NOT NULL,
	Id_Cargo INT NOT NULL,
	Data_Cadatro datetime NOT NULL,
	Dt_Contratacao datetime NOT NULL,
	status VARCHAR NOT NULL,
	Data_Recisao datetime,
	FOREIGN KEY (Id_Cargo) REFERENCES Cargo(Id_Cargo)
);

CREATE TABLE Medico (
	Id_Medico int PRIMARY KEY NOT NULL,
	Nome VARCHAR NOT NULL,
	Sobrenome VARCHAR NOT NULL,
	Genero VARCHAR,
	CPF VARCHAR NOT NULL,
	Data_Nascimento date NOT NULL,
	Telefone VARCHAR,
	Celular VARCHAR,
	Email VARCHAR NOT NULL,
	CRM VARCHAR NOT NULL,
	RQE VARCHAR NOT NULL,
	Id_especialidade INT NOT NULL,
	Data_Cadatro datetime NOT NULL,
	Data_Contratacao datetime NOT NULL,
	status VARCHAR NOT NULL,
	Data_Recisao datetime,
	FOREIGN KEY (Id_especialidade) REFERENCES Especialidade(Id_Especialidade)
);

CREATE TABLE Paciente (
	Id_Paciente int PRIMARY KEY NOT NULL,
	Nome VARCHAR NOT NULL,
	Sobrenome VARCHAR NOT NULL,
	Genero VARCHAR,
	CPF VARCHAR NOT NULL,
	Data_Nascimento date NOT NULL,
	Telefone VARCHAR,
	Celular VARCHAR,
	Email VARCHAR NOT NULL,
	Endereco VARCHAR NOT NULL,
	Num_Convenio VARCHAR,
	Id_Convenio INT NOT NULL,
	Id_Prescricao INT,
	Data_Cadatro datetime NOT NULL,
	status VARCHAR NOT NULL,
	FOREIGN KEY (Id_Convenio) REFERENCES Convenio(Id_Convenio),
	FOREIGN KEY (Id_Prescricao) REFERENCES Prescricao(Id_Prescricao)
);

CREATE TABLE Administrador (
	Id_Adm int PRIMARY KEY NOT NULL,
	Nome VARCHAR NOT NULL,
	Sobrenome VARCHAR NOT NULL,
	Genero VARCHAR,
	CPF VARCHAR NOT NULL,
	Data_Nascimento date NOT NULL,
	Telefone VARCHAR,
	Celular VARCHAR,
	Email VARCHAR NOT NULL,
	Data_Cadatro datetime NOT NULL,
	Data_Contratacao datetime NOT NULL,
	status VARCHAR NOT NULL,
	Data_Recisao datetime
);


CREATE TABLE Consulta (
	Id_Consulta int PRIMARY KEY NOT NULL,
	Data datetime NOT NULL,
	Hora time NOT NULL,
	Id_Paciente INT NOT NULL,
	Id_Medico INT NOT NULL,
	Id_Especialidade INT NOT NULL,
	Id_Convenio INT NOT NULL,
	Id_Prescricao INT NOT NULL,
	Valor float NOT NULL,
	Status VARCHAR NOT NULL,
	FOREIGN KEY (Id_Paciente) REFERENCES Paciente(Id_Paciente) ,
	FOREIGN KEY (Id_Medico) REFERENCES Medico(Id_Medico),
	FOREIGN KEY (Id_Especialidade) REFERENCES Especialidade(Id_Especialidade),
	FOREIGN KEY (Id_Convenio) REFERENCES Convenio(Id_Convenio),
	FOREIGN KEY (Id_Prescricao) REFERENCES Prescricao(Id_Prescricao)
);












