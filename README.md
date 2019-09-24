# tutorial_http_server
Vamos aprender como criar e configurar um servidor HTTP. Mas antes disso vamos revisar alguns conceitos.

## O que é Rede de Computadores?
Interligação de dois ou mais computadores e seus perifericos, com o objetivo de comunicação e compartilhamento de dados.

## Como funciona?

Para que essa interligação funcione de maneira ordenada, existem uma série de regras para que essa comunicação seja feita de maneira correta. 

A comunicação é feita em etapas por meio de camadas e protocolos. 

As camadas são:

| Camada |         Protocol |           Protocol Data Unit |     Addressing|
|--------|------------------|------------------------------|---------------|
|Application|     HTTP, SMTP, etc|     Messages |               NA |  
|Transport|       TCP, UDP|            Segment |                 Port # |
|Network|         IP|                  Datagram |                IP adress |  
|Data Link|       Ethernet, Wifi|      Frames |                  MAC adress |
|Physical|                       |     Bits |                     NA |



### Protocolos
Protocolos definem regras que:
- estabelece o formato e a ordem das mensagens as ações a serem tomadas na transmissão e recepção das mensagens


## HTTP- HyperText Transfer Protocol 
Segundo Tanembaum:

"O protocolo de transferência utilizado em toda a World Wide Web é o HTTP (HyperText Transfer
Protocol). Ele especifica as mensagens que os clientes podem enviar aos servidores e que respostas
eles receberão. Cada interação consiste em uma solicitação ASCII, seguida por uma resposta RFC
822 semelhante ao MIME. Todos os clientes e todos os servidores devem obedecer a esse protocolo.
Ele é definido na RFC 2616."

![Drag Racing](images/Fetching_a_page.jpg)

Os métodos internos de solicitações HTTP:

| Método| Descrição |
| ------|---------- |
| GET | Solicita a leitura de uma página da Web |
| HEAD | Solicita a leitura de um cabeçalho de página da Web |
| PUT | Solicita o armazenamento de uma página da Web | 
| POST | Acrescenta a um recurso (por exemplo, uma página da Web) |
| DELETE | Remove a página da Web | 
| TRACE | Ecoa a solicitação recebida |
| CONNECT | Reservado para uso futuro |
| OPTIONS | Consulta certas opções |



 Os grupos de respostas de código de status:
 
| Código | Significado | Exemplos |
| -------| ------------ | --------- |
| 1xx | Informação | 100 = server agrees to handle client's request |
| 2xx | Sucesso | 200 = request succeeded; 204 = no content present |
| 3xx | Redirecionamento | 301 = page moved; 304 = cached page still valid |
| 4xx | Erro do cliente | 403 = forbidden page; 404 = page can not found |
| 5xx | Erro do servidor | 500 = internal server error; 503 = try again later |

