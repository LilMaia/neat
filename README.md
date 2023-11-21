# NEAT

Neste projeto, é aplicado o algoritmo NEAT para treinar agentes em um ambiente do jogo (Daffy Duck: The Marvin Missions). O NEAT, que significa NeuroEvolution of Augmenting Topologies, difere do método tradicional de treinamento de redes neurais, pois evolui a arquitetura da rede ao longo do tempo. Cada agente no NEAT é representado por dois conjuntos de genes: nós (neurônios) e conexões entre esses nós. O treinamento ocorre por meio de mutações e cruzamentos, sem a necessidade de treinamento supervisionado. O projeto visa explorar a capacidade do NEAT em descobrir automaticamente arquiteturas eficazes para tarefas complexas, oferecendo uma abordagem adaptativa e autônoma para o aprendizado de máquina.

# Configuração do ambiente

Para a execução deste projeto, foi essencial estabelecer um ambiente de desenvolvimento local no sistema operacional Windows 11. A implementação contou com a utilização do Python 3.8, além das bibliotecas Gym na versão 0.21.0 e Gym Retro na versão 0.8.0. Importante ressaltar que versões mais recentes dessas bibliotecas são incompatíveis com as versões anteriores.

Após a configuração do ambiente, tornou-se necessário adquirir uma ROM do jogo Daffy Duck: The Marvin Missions, escolhido para os testes. A ROM precisa coincidir com a SHA1 determinada pelo Gym Retro em suas instalações para o respectivo jogo.

![Alt Text](prints_readme/SHA1.png)

Com o ambiente e o jogo devidamente configurados, o próximo passo consiste na compilação e execução do código Python. Basta abrir o prompt de comando na pasta onde todas as configurações foram realizadas, digitar "Scripts\activate" e pressionar "Enter". Em seguida, o código pode ser executado acessando o diretório onde o código está localizado e utilizando o comando "python nome_do_arquivo.py".

![Alt Text](prints_readme/comandos.png)

![Alt Text](prints_readme/executando.png)
