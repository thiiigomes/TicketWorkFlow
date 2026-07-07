# Casos de Uso

## Objetivo 

Este documento descreve os principais fluxos de utilização do sistema Ticket WorkFlow.

Cada caso de uso representa uma interação entre um usuário e o sistema, descrevendo as etapas necessárias para a execução de uma funcionalidade.

## UC001 - Abrir Chamado

**Ator Principal:** Usuário

**Objetivo:**
Permitir que um usuário registre um novo chamado de suporte.

**Pré-condições:**
- O usuário deve estar autenticado no sistema.

**Observação:**
- Durante a abertura do chamado, os campos exibidos variam conforme a categoria selecionada, conforme definido na RN010.

**Fluxo Principal:**

1. O usuário acessa a tela de abertura de chamados.
2. O sistema apresenta o formulário de abertura.
3. O usuário seleciona a categoria do problema.
4. O sistema exibe os campos específicos conforme a categoria.
5. O usuário preenche as informações solicitadas.
6. O usuário envia o chamado.
7. O sistema registra o chamado.
8. O sistema define o status do chamado como **Aberto**.
9. O sistema coloca o chamado na fila de atendimento.
10. O sistema confirma a abertura do chamado.

**Pós-condições:**

- O chamado é criado com sucesso.
- O chamado fica disponível para atendimento.
