

  Aqui está a nota de atualização referente às funções de **Potenciação** e **Porcentagem**, seguindo o mesmo estilo e estrutura do seu texto:

---

# Atualização da Calculadora — v1.2

## Novidades

* **Adicionadas as funções de Potenciação e Porcentagem**: agora é possível elevar um número a uma potência e calcular percentuais diretamente pelo menu (opções 7 e 8).

## Correções de bugs

* **Tratamento no envio dos parâmetros**: corrigido o problema onde os nomes das variáveis no menu causam confusão na leitura. Na porcentagem, os valores agora são repassados explicitamente como `total` e `percentual` para evitar inversão no cálculo.

## Melhorias técnicas

* Criados os métodos `potenciacao()` e `porcentagem()` na classe `Calculadora`, mantendo o padrão visual das demais funções com o `limpar_console()` e a exibição da mensagem descritiva no console antes do retorno.
* Texto do menu e validação de `input()` atualizados para incluir as novas opções (1 a 8).

## Observação conhecida

* Na função de porcentagem, a ordem de entrada dos números importa (primeiro o valor total, depois o percentual desejado). A interface será ajustada em versões futuras para deixar esse fluxo mais intuitivo.