def notas(*nota, situacao = False):  
    """
    -> Função para analisar notas e situação de aluno.
    :param nota: uma ou mais notas dos alunos.
    :param situcao: (opcional) Mostra situação do aluno, conforme média.
    :return: retorna dicionário com total, maior, menor e média de notas e situação se necessário.
    """
    boletim = {}
    media = sum(nota)/len(nota)
    boletim['total'] = len(nota) - 1
    boletim['maior'] = max(nota)
    boletim['menor'] = min(nota)
    boletim['media'] = media
    if situacao == True:
        if media >= 7:
            boletim['situacao'] = 'BOA'
        elif 7 > media >= 5:
            boletim['situacao'] = 'MEDÍOCRE'
        else:
            boletim['situacao'] = 'RUIM'
    return boletim

print(notas(1,2,3, True))
help(notas)
