MEDIA DE NOTA POR CASA - OK
Listagem da Casa
Quem tem tutor - OK
Origem da Família   - OK
Especies de Animais
Qual Professor Mais Velho de cada Casa - MAX  - OK
Qual Aluno Mais NOVO da Escola - MIN

---------------- CONSULTAS --------------------

-- 1) Média de notas por aluno 
SELECT A.nome_aluno AS Aluno, AVG(B.nota) AS [Nota Média] FROM
Tb_ALUNOS A INNER JOIN Tb_ALUNOS_NOTAS B
ON A.id_aluno = B.id_aluno
GROUP BY A.NOME_ALUNO
ORDER BY AVG(B.nota) DESC;


-- 2) Média das notas por casa
SELECT D.nome_casa AS Casa, AVG(B.NOTA) AS [Nota Média] FROM
Tb_ALUNOS A INNER JOIN Tb_ALUNOS_NOTAS B
ON A.id_aluno = B.id_aluno 
INNER JOIN 
[Tb_CASAS] D
ON A.id_casa = D.id_casa
GROUP BY D.nome_casa;


-- 3) Distribuição do tipo de sangue dos alunos
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
AS  [Mestiço]
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


-- 5) Nota média por matéria
SELECT A.nome_materia AS [Matéria], ROUND(AVG(B.nota), 2) AS [Média de Notas] FROM
Tb_MATERIAS A INNER JOIN Tb_ALUNOS_NOTAS B
ON A.id_materia = B.id_materia
GROUP BY A.nome_materia
ORDER BY [Média de Notas] DESC;


-- 6) Número de Alunos por casa
SELECT A.nome_casa AS Casa, COUNT(*) AS [Número de Alunos] FROM 
Tb_CASAS A INNER JOIN Tb_ALUNOS B
ON A.id_casa = B.id_casa
GROUP BY A.nome_casa;

/*
-- 7) Animal mais comum em cada casa
SELECT A.nome_casa AS Casa, C.especie_animal AS [Espécie] , COUNT(*) AS Quantidade FROM
Tb_CASAS A INNER JOIN Tb_ALUNOS B
ON A.id_casa = B.id_casa
INNER JOIN Tb_ANIMAIS C
ON C.id_animal = B.id_animal
GROUP BY A.nome_casa, C.especie_animal
ORDER BY Casa, Quantidade;

-- 8) Especie mais comum por casa
SELECT A.nome_casa AS Casa, C.especie_animal AS [Espécie] , COUNT(especie_animal) AS Quantidade, RANK() OVER (
            PARTITION BY nome_casa
            ORDER BY COUNT(especie_animal)) especie_rank
FROM
Tb_CASAS A INNER JOIN Tb_ALUNOS B
ON A.id_casa = B.id_casa
INNER JOIN Tb_ANIMAIS C
ON C.id_animal = B.id_animal
GROUP BY A.nome_casa, C.especie_animal
*/

