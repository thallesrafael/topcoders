USE HOGWARTS

CREATE TABLE Tb_CLASSES(
	id_classe INT IDENTITY(1000,1) NOT NULL,
	nome_classe varchar(50) NOT NULL,
	PRIMARY KEY (id_classe)
);

CREATE TABLE Tb_MATERIAS(
	id_materia INT IDENTITY(2000,1) NOT NULL,
	nome_materia varchar(50) NOT NULL,
	PRIMARY KEY (id_materia)
);

CREATE TABLE Tb_CLASSES_MATERIAS(
	id_classe INT FOREIGN KEY REFERENCES Tb_CLASSES(id_classe),
	id_materia INT FOREIGN KEY REFERENCES Tb_MATERIAS(id_materia),
	carga_horaria INT NOT NULL,
	PRIMARY KEY(id_classe, id_materia)
);


CREATE TABLE Tb_TUTORES(
	id_tutor INT IDENTITY (3000, 1) NOT NULL,
	nome_tutor varchar(255) NOT NULL,
	bruxo BIT NOT NULL,
	PRIMARY KEY (id_tutor) 
);

CREATE TABLE Tb_PROFESSORES(
	id_professor INT IDENTITY (4000, 1) NOT NULL,
	nome_professor VARCHAR(255) NOT NULL,
	data_de_nascimento_professor DATE,
	PRIMARY KEY (id_professor),
	id_materia INT FOREIGN KEY REFERENCES Tb_MATERIAS(id_materia)
);

CREATE TABLE Tb_ANIMAIS(
	id_animal INT IDENTITY(5000,1) NOT NULL,
	nome_animal VARCHAR(255) NOT NULL,
	especie_animal VARCHAR(255) NOT NULL,
	idade_animal INT NOT NULL,
	PRIMARY KEY (id_animal)
);

CREATE TABLE Tb_PAIS(
	id_pais INT IDENTITY(5000,1) NOT NULL,
	nome_pai VARCHAR(255) NOT NULL,
	nome_mae VARCHAR(255) NOT NULL,
	data_de_nascimento_pai DATE,
	data_de_nascimento_mae DATE,
	mae_bruxa BIT NOT NULL,
	pai_bruxo BIT NOT NULL,
	PRIMARY KEY (id_pais)
);

CREATE TABLE Tb_ALUNOS(
	id_aluno INT IDENTITY(6000,1) NOT NULL,
	nome_aluno VARCHAR(255) NOT NULL,
	data_nascimento_aluno DATE NOT NULL,
	endereco VARCHAR(1000) NOT NULL,
	id_classe INT FOREIGN KEY REFERENCES Tb_CLASSES(id_classe),
	id_animal INT FOREIGN KEY REFERENCES Tb_ANIMAIS(id_animal),
	id_tutor INT FOREIGN KEY REFERENCES Tb_TUTORES(id_tutor),
	id_pais	INT FOREIGN KEY REFERENCES Tb_PAIS(id_pais)
	PRIMARY KEY (id_aluno)
);

CREATE TABLE Tb_CASAS(
	id_casa int IDENTITY(1,1) NOT NULL,
	nome_casa varchar(50) NOT NULL,
	tipo_personalidade varchar(150) NOT NULL,
	brasao varchar(50) NOT NULL,
	cor varchar(20) NOT NULL,
	diretor int FOREIGN KEY REFERENCES Tb_PROFESSORES(id_professor),
	monitor int FOREIGN KEY REFERENCES Tb_ALUNOS(id_aluno),
	PRIMARY KEY (id_casa)
);

ALTER TABLE Tb_PROFESSORES
	ADD id_casa INT FOREIGN KEY REFERENCES Tb_CASAS(id_casa);

ALTER TABLE Tb_ALUNOS
	ADD id_casa INT FOREIGN KEY REFERENCES Tb_CASAS(id_casa);

CREATE TABLE Tb_ALUNOS_NOTAS(
	id_aluno INT FOREIGN KEY REFERENCES Tb_alunos(id_aluno),
	id_materia INT FOREIGN KEY REFERENCES Tb_MATERIAS(id_materia),
	nota FLOAT,
	PRIMARY KEY(id_aluno, id_materia)
);