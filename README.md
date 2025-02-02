# Code Stresser - Teste de Ataque de Rede

O **Code Stresser** é uma ferramenta web projetada para testar a proteção de servidores contra ataques DDoS (Distributed Denial of Service). Ela permite simular diferentes tipos de ataques, como HTTP Flood, SYN Flood, UDP Flood e Slowloris, para verificar a resistência de sistemas de rede e a eficácia de defesas Anti-DDoS.

Este projeto é destinado para fins educativos e de testes em ambientes controlados, como servidores próprios ou ambientes isolados. Não use esta ferramenta em redes de terceiros sem autorização expressa, pois isso pode ser ilegal.

## Funcionalidades

- **Tipo de Ataque**: Escolha entre 4 tipos de ataques DDoS:
  - HTTP Flood
  - SYN Flood
  - UDP Flood
  - Slowloris
- **Configuração de Porta**: Defina a porta de destino (ou use a porta aleatória definindo `0`).
- **Número de Threads**: Controle o número de threads para o ataque, variando entre 1 e 1000.
- **Duração do Ataque**: Defina a duração do ataque, de 1 até 3600 segundos.
- **Interface Web**: Interface simples e intuitiva para facilitar a configuração e execução dos testes de ataque.

## Requisitos

- **Servidor**: Pode ser hospedado em qualquer servidor capaz de rodar Flask.
- **Tecnologias Usadas**:
  - **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
  - **Backend**: Flask (Python)

## Como Usar

### Passo 1: Clone o Repositório

Clone este repositório para o seu ambiente local ou servidor.

```bash
git clone https://github.com/SeuUsuario/CodeStresser.git
cd CodeStresser
```

### Passo 2: Instale as Dependências

Instale as dependências necessárias para rodar o servidor Flask.

```bash
pip install -r requirements.txt
```

### Passo 3: Execute o Servidor Flask

Inicie o servidor Flask para rodar a interface web.

```bash
python app.py
```

O servidor estará disponível em `http://127.0.0.1:5000` ou no IP configurado em seu ambiente.

### Passo 4: Acesse a Interface Web

Abra o navegador e acesse o endereço `http://127.0.0.1:5000`. Você verá a interface de ataque onde pode configurar os parâmetros do ataque.

- **Endereço IP de Destino**: Insira o endereço IP do servidor que deseja testar.
- **Porta**: Defina a porta ou use `0` para uma porta aleatória.
- **Tipo de Ataque**: Selecione o tipo de ataque que deseja realizar.
- **Número de Threads**: Defina o número de threads para o ataque.
- **Duração**: Especifique por quanto tempo o ataque deve ocorrer.

Clique em "Iniciar Ataque" para iniciar o ataque.

## Como Contribuir

1. Faça o fork deste repositório.
2. Crie uma branch para a sua feature (`git checkout -b minha-feature`).
3. Faça as alterações necessárias e commit (`git commit -am 'Adicionando uma nova feature'`).
4. Envie a sua branch para o repositório remoto (`git push origin minha-feature`).
5. Abra um Pull Request.

## Aviso Legal

Este projeto foi desenvolvido para fins educacionais e de testes em um ambiente controlado. O uso indevido da ferramenta para realizar ataques a servidores sem permissão é ilegal e pode resultar em penalidades criminais. A responsabilidade pelo uso da ferramenta é inteiramente do usuário.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```

