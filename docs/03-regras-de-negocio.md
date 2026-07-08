# Regras de Negócio

## Objetivo 

Este documento descreve as regras de negócio do sistema Ticket WorkFlow.

As regras definem os comportamentos, restrições e políticas que deverão ser respeitados durante a utilização do sistema.

## Gestão de Chamados

RN001 - Todo chamado deverá possuir uma prioridade.

RN002 - A prioridade definitiva do chamado será definida pelo técnico responsável após a análise inicial.

RN003 - O sistema deverá monitorar chamados sem movimentação.

RN004 - Caso um chamado permaneça sem movimentação por um período determinado, o sistema deverá notificar o técnico responsável.

RN005 - Persistindo a ausência de movimentação, o chamado deverá ser escalonado automaticamente para o gestor responsável.

RN006 - Um chamado poderá possuir apenas um técnico responsável por vez.

RN007 - A transferência de um chamado para outro técnico somente poderá ser realizado pelo técnico responsável ou por administradores.

RN008 - Todo equipamento deverá possuir um histórico completo de atendimentos.

RN009 - O sistema deverá identificar equipamentos com recorrência de falhas e emitir um alerta para avaliação técnica.

RN010 - As informações solicitadas na abertura do chamado deverão variar conforme a categoria selecionada.

RN011 - Todo chamado deverá possuir um status.

RN012 - Um chamado somente poderá ser encerrado após possuir uma solução registrada.

RN013 - Todo atendimento deverá registrar data, hora e responsável por cada movimentação realizada.

RN014 - Todo equipamento deverá possuir um número de patrimônio único.

RN015 - Usuários não poderão alterar o chamado após um técnico assumir o atendimento.

RN016 - Chamados sem atualização por período superior ao SLA deverão ser destacados na Central de Atendimento e priorizados pelo sistema.

RN017 - Chamados encerrados não poderão ser excluídos do sistema.

RN018 - Todas as mensagens trocadas entre usuário e técnico deverão permancer registradas no histórico do chamado.

RN019 - Sempre que o técnico solicitar informações adicionais ao usuário, o status do chamado deverá ser alterado para "Aguardando Usuário".

RN020 - Após a resposta do usuário, o chamado deverá retornar automaticamente para o status "Em Atendimento".

RN021 - Caso um chamado seja reaberto, o sistema deverá notificar automaticamente o gestor responsável.

RN022 - Todo chamado reaberto deverá manter o histórico completo do atendimento anterior.

RN023 - O comentário do usuário sobre o atendimento será opcional, ficará vinculado ao histórico do chamado e poderá ser colsutado pelo gestor e pelo técnico responsável.