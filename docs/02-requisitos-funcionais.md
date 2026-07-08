# Requisitos Funcionais

Este documento descreve todos os requisitos funcionais do sistema Ticket Workflow.

Cada requisito funcional representa uma funcionalidade que deverá ser implementada durante o desenvolvimento do projeto.


## Módulo: Autenticação

RF001 - O sistema deverá permitir que usuários realizem login utilizando e-mail e senha.

RF002 - O sistema deverá permitir que usuários encerrem sua sessão por meio da funcionalidade do logout.

RF003 - O sistema deverá controlar o acesso às funcionalidades conforme o perfil do usuário.

## Gestão de Chamados

RF004 - O sistema deverá permitir que o usuário acompanhe o andamento do chamado em tempo real.

RF005 - O sistema deverá exibir o técnico responsável pelo atendimento.

RF006 - O sistema deverá registrar e exibir todas as ações realizadas durante o atendimento.

RF007 - O sistema deverá informar a solução aplicada ao chamado.

RF008 - O sistema deverá permitir registrar o destino do equipamento, como reparo, substituição ou devolução ao usuário.


## Gestão de Usuários

RF009 - O sistema deverá permitir cadastrar usuários.

RF010 - O sistema deverá permitir editar usuários.

RF011 - O sistema deverá permitir inativar usuários.

RF012 - O sistema deverá permitir consultar usuários cadastrados.


## Gestão de Ativos

RF013 - O sistema deverá permitir cadastrar equipamentos.

RF014 - O sistema deverá permitir vincular um equipamento a um usuário.

RF015 - O sistema deverá permitir consultar o histórico de um equipamento.

RF016 - O sistema deverá permitir alterar a situação do equipamento.


## Dashboard 

RF017 - O sistema deverá apresentar indicadores de chamados por status.

RF018 - O sistema deverá apresentar indicadores por prioridade.

RF019 - O sistema deverá apresentar indicadores por departamento.

RF020 - O sistema deverá apresentar indicadores por técnico.

## Gestão de Chamados

RF021 - O sistema deverá permitir que usuários abram novos chamados.

RF022 - O sistema deverá permitir anexar imagens ou arquivos ao chamado.

RF023 - O sistema deverá permitir adicionar comentários ao chamado durante o atendimento.

RF024 - O sistema deverá permitir alterar o status do chamado.

RF025 - O sistema deverá permitir pesquisar equipamentos pelo patrimônio ou número de série.

RF026 - O sistema deverá permitir redefinir a senha de usuários.

RF027 - O sistema deverá solicitar a identificação do equipamento durante a abertura do chamado.

RF028 - O sistema deverá permitir informar as tentativas de solução realizadas pelo usuário antes de abertura do chamado.

RF029 - O sistema deverá permitir a troca de mensagens entre o técnico e o usuário durante o atendimento do chamado.

RF030 - O sitema deverá permitir que o usuário registre um comentário sobre o atendimento após o encerramento do chamado.

Perfis disponíveis:

- Usuário
- Técnico
- Administrador