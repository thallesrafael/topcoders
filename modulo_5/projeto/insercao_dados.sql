USE HOGWARTS

INSERT INTO Tb_TUTORES(nome_tutor,bruxo)
 VALUES ('Válter Dursley', 0)

INSERT INTO Tb_PAIS(nome_pai, nome_mae, data_de_nascimento_mae, data_de_nascimento_pai, mae_bruxa, pai_bruxo)
VALUES	('Tiago Potter', 'Lílian Evans Potter', '1960-01-30', '1960-03-27', 1, 1),
		('Xenofílio Lovegood', 'Pandora Lovegood', '1960-02-16', '1964-02-03', 1, 1),		
		('Amos Diggory', 'Taís Diggory', '1960-09-01', '1960-09-30', 1, 1),
		('Lucius Malfoy', 'Narcissa Malfoy', '1955-01-01', '1953-09-09', 1, 1),
		('Wendell Granger', 'Monica Granger', '1959-07-05', '1960-03-17', 0, 0),
		('Colm Abbott', 'Adda Abbott', '1952-05-05', '1954-07-18', 0, 1),
		('Hari Patil', 'Kali Patil', '1954-11-03', '1955-02-16', 1, 1),
		('Bartley Parkinson', 'Aileen Parkinson', '1955-10-19', '1955-12-10', 1, 1)
		
INSERT INTO Tb_ANIMAIS(nome_animal,especie_animal,idade_animal)
VALUES	('Edwiges','Coruja', 8),
		('Pigwidgeon','Coruja', 7),
		('Lu','Coruja',9),
		('Pen','Rato',5),
		('Bichento','Gato', 5),
		('Ott','Coruja', 7),
		('Powk','Gato', 4),
		('Owl','Coruja', 8)

INSERT INTO Tb_MATERIAS(nome_materia)
VALUES	('Tranfiguração'),
		('Herbologia'),
		('Feitiços'),
		('Porções')

INSERT INTO Tb_CLASSES(nome_classe)
VALUES	('1 ano'),
		('2 ano'),
		('3 ano'),
		('4 ano')

ALTER TABLE Tb_CLASSES_MATERIAS NOCHECK CONSTRAINT ALL 

INSERT INTO Tb_CLASSES_MATERIAS(id_classe, id_materia, carga_horaria)
VALUES	(1000,2000,70),
		(1000,2001,60),
		(1000,2002,80),
		(1000,2003,100),
		(1001,2000,60),
		(1001,2001,60),
		(1001,2002,75),
		(1001,2003,85),
		(1002,2000,90),
		(1002,2001,50),
		(1002,2002,65),
		(1002,2003,75),
		(1003,2000,80),
		(1003,2001,90),
		(1003,2002,60),
		(1003,2003,60)

ALTER TABLE Tb_CLASSES_MATERIAS CHECK CONSTRAINT ALL 

INSERT INTO Tb_PROFESSORES (nome_professor, data_de_nascimento_professor)
VALUES  ('Minerva McGonagall', '1935-10-04'),
	    ('Pomona Sprout', '1931-05-15'),
	    ('Filius Flitwick', '1958-10-17'),        
	    ('Severo Snape', '1960-09-01');
        
INSERT INTO Tb_CASAS(nome_casa,tipo_personalidade, brasao, cor, diretor, monitor)
VALUES		('Grifinória', 'coragem, ousadia, determinação, audácia e atrevimento', 'Leão', 'Vermelho e Dourado', NULL, NULL ),
			('Lufa-Lufa', 'leais, trabalhadores, pacientes, justos, dedicados e verdadeiros', 'Texugo', 'Amarelo e o Preto', NULL, NULL ),
			('Corvinal', 'inteligentes, criativos, perspicazes, prudentes e estudiosos', 'Águia', 'Azul e o Bronze', NULL, NULL),
			('Sonserina', 'ambição, astúcia, liderança, desembaraço e individualismo', 'Serpente', 'Verde e o Prateado', NULL, NULL )
	

ALTER TABLE Tb_ALUNOS NOCHECK CONSTRAINT ALL 

INSERT INTO Tb_ALUNOS( nome_aluno, data_nascimento_aluno, endereco, id_classe, id_animal, id_tutor, id_pais, id_casa)
VALUES	('Harry Tiago Potter', '1980-07-31', 'Inglaterra', 1001, 5000, 3000, 5000, 1),
		('Luna Lovegood', '1981-02-13', 'Grã-Bretanha', 1000, 5001, NULL, 5001, 2),
		('Cedrico Diggory', '1977-09-01', 'Gra-Bretanha',1003, 5002, NULL, 5002, 3),
		('Draco Lucius Malfoy', '1980-06-05', 'Gra-Bretanha', 1001, 5003, NULL, 5003, 4),
		('Hermione Jean Granger', '1979-09-19', 'Inglaterra', 1001, 5004, NULL, 5004, 1),
		('Ana Abbott', '1979-09-15', 'Gra-Bretanha', 1002, 5005, NULL, 5005, 2),
		('Padma Patil', '1980-04-21', 'Irlanda', 1001, 5006, NULL, 5006, 3),
		('Pansy Parkinson', '1980-08-31', 'Inglaterra', 1001, 5007, NULL, 5007, 4);

ALTER TABLE Tb_ALUNOS NOCHECK CONSTRAINT ALL 



UPDATE Tb_CASAS
SET diretor = 4000, monitor =  6004
WHERE id_casa = 1;

UPDATE Tb_CASAS
SET diretor = 4001, monitor =  6005
WHERE id_casa = 2;

UPDATE Tb_CASAS
SET diretor = 4002, monitor =  6006
WHERE id_casa = 3;

UPDATE Tb_CASAS
SET diretor = 4003, monitor =  6007
WHERE id_casa = 4;

ALTER TABLE Tb_PROFESSORES NOCHECK CONSTRAINT ALL 

UPDATE Tb_PROFESSORES
SET ID_CASA = CASE 
WHEN ID_PROFESSOR = 4000 THEN 1
WHEN ID_PROFESSOR = 4001 THEN 2
WHEN ID_PROFESSOR = 4002 THEN 3
WHEN ID_PROFESSOR = 4003 THEN 4
END

UPDATE Tb_PROFESSORES
SET ID_MATERIA = CASE 
WHEN ID_PROFESSOR = 4000 THEN 2000
WHEN ID_PROFESSOR = 4001 THEN 2001
WHEN ID_PROFESSOR = 4002 THEN 2002
WHEN ID_PROFESSOR = 4003 THEN 2003
END

ALTER TABLE Tb_PROFESSORES CHECK CONSTRAINT ALL 

INSERT INTO Tb_ALUNOS_NOTAS (id_aluno, id_materia)
SELECT A.ID_ALUNO, B.ID_MATERIA FROM
Tb_ALUNOS A CROSS JOIN Tb_MATERIAS B
ORDER BY A.id_aluno ASC;


UPDATE Tb_ALUNOS_NOTAS
SET    nota = abs(checksum(NewId()) % 10) + 2

UPDATE Tb_ALUNOS_NOTAS
SET nota = CASE 
WHEN nota > 10 THEN 10
ELSE nota
END;

UPDATE Tb_ALUNOS_NOTAS
SET nota = CASE 
WHEN ID_ALUNO = 6004 THEN 10
ELSE nota
END;
