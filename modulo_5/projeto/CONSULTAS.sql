MEDIA DE NOTA POR CASA - OK
Listagem da Casa
Quem tem tutor - OK
Origem da Fam�lia   - OK
Especies de Animais
Qual Professor Mais Velho de cada Casa - MAX  - OK
Qual Aluno Mais NOVO da Escola - MIN

---------------- CONSULTAS --------------------

-- 1) M�dia de notas por aluno 
SELECT A.nome_aluno AS Aluno, AVG(B.nota) AS [Nota M�dia] FROM
Tb_ALUNOS A INNER JOIN Tb_ALUNOS_NOTAS B
ON A.id_aluno = B.id_aluno
GROUP BY A.NOME_ALUNO
ORDER BY AVG(B.nota) DESC;


-- 2) M�dia das notas por casa
SELECT D.nome_casa AS Casa, AVG(B.NOTA) AS [Nota M�dia] FROM
Tb_ALUNOS A INNER JOIN Tb_ALUNOS_NOTAS B
ON A.id_aluno = B.id_aluno 
INNER JOIN 
[Tb_CASAS] D
ON A.id_casa = D.id_casa
GROUP BY D.nome_casa;


-- 3) Distribui��o do tipo de sangue dos alunos
SELECT 
C.nome_casa AS [Casa],
SUM(CASE 
WHEN (CONVERT(INT, B.mae_bruxa) + CONVERT(INT, B.pai_bruxo)) < 2 THEN 0
WHEN (CONVERT(INT, B.mae_bruxa) + CONVERT(INT, B.pai_bruxo)) = 2 THEN 1
end)
AS  [Sangue puro],
SUM(CASE 
WHEN (CONVERT(INT, B.mae_bruxa) + CONVERT(INT, B.pai_bruxo)) < 2 THEN 1
WHEN (CONVERT(INT, B.mae_bruxa) + CONVERT(INT, B.pai_bruxo)) = 2 THEN 0
end)
AS  [Mesti�o]
FROM 
Tb_ALUNOS A INNER JOIN Tb_PAIS B 
ON A.id_pais = B.id_pais
INNER JOIN Tb_CASAS C
ON A.id_casa = C.id_casa
GROUP BY C.nome_casa
ORDER BY [Casa];


-- 4) Professor mais velho de cada casa
SELECT tc.nome_casa AS Casa, tp.nome_professor AS Professor, DATEDIFF(year, data_de_nascimento_professor, GETDATE()) AS Idade
FROM Tb_CASAS tc inner join Tb_PROFESSORES tp 
on tc.id_casa = tp.id_casa
ORDER BY tc.nome_casa;


-- 5) Nota m�dia por mat�ria
SELECT A.nome_materia AS [Mat�ria], ROUND(AVG(B.nota), 2) AS [M�dia de Notas] FROM
Tb_MATERIAS A INNER JOIN Tb_ALUNOS_NOTAS B
ON A.id_materia = B.id_materia
GROUP BY A.nome_materia
ORDER BY [M�dia de Notas] DESC;


-- 6) N�mero de Alunos por casa
SELECT A.nome_casa AS Casa, COUNT(*) AS [N�mero de Alunos] FROM 
Tb_CASAS A INNER JOIN Tb_ALUNOS B
ON A.id_casa = B.id_casa
GROUP BY A.nome_casa;

/*
-- 7) Animal mais comum em cada casa
SELECT A.nome_casa AS Casa, C.especie_animal AS [Esp�cie] , COUNT(*) AS Quantidade FROM
Tb_CASAS A INNER JOIN Tb_ALUNOS B
ON A.id_casa = B.id_casa
INNER JOIN Tb_ANIMAIS C
ON C.id_animal = B.id_animal
GROUP BY A.nome_casa, C.especie_animal
ORDER BY Casa, Quantidade;

-- 8) Especie mais comum por casa
SELECT A.nome_casa AS Casa, C.especie_animal AS [Esp�cie] , COUNT(especie_animal) AS Quantidade, RANK() OVER (
            PARTITION BY nome_casa
            ORDER BY COUNT(especie_animal)) especie_rank
FROM
Tb_CASAS A INNER JOIN Tb_ALUNOS B
ON A.id_casa = B.id_casa
INNER JOIN Tb_ANIMAIS C
ON C.id_animal = B.id_animal
GROUP BY A.nome_casa, C.especie_animal
*/

