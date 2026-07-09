

  Atualização da Calculadora — v1.1
   Novidades
 **Adicionada a função de Raiz Quadrada**: agora é possível calcular a raiz quadrada de um número diretamente pelo menu (opção 5).

 Correções de bugs
- **Opção 5 corrigida**: antes, ao escolher "5. Raiz quadrada", o programa encerrava a execução por engano (esse comportamento pertencia à opção de sair). Agora a opção 5 realmente calcula a raiz quadrada.
- **Opção 6 implementada**: a opção "Sair" agora está corretamente vinculada ao número 6, que antes não tinha nenhum tratamento e caía na mensagem de "escolha inválida".

# Melhorias técnicas
- Importada a biblioteca `math` para uso da função `math.sqrt()`.
- Criado o método `raiz_quadrada()` na classe `Calculadora`, seguindo o mesmo padrão visual (limpeza de console + mensagem) dos demais métodos.
- Texto de input do menu atualizado para refletir todas as opções disponíveis (1 a 6).

# Observação conhecida
- O programa ainda solicita dois números antes de exibir o menu, mesmo quando a operação escolhida (como a raiz quadrada) só usa um deles. Isso não afeta o funcionamento, mas pode ser ajustado futuramente para melhorar a experiência do usuário.
