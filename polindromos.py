palavra = input("Digite uma palavra: ").lower()

if palavra == palavra[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

# Exemplo de palíndromo: "arara"

# Exemplo de não palíndromo: "python"

# qual é a diferença entre palíndromo e não palíndromo?

# Um palíndromo é uma palavra, frase, número ou qualquer outra sequência de caracteres que lê o mesmo de trás para frente e 
# de frente para trás, ignorando espaços, pontuação e diferenças entre maiúsculas e minúsculas. Por exemplo, "arara" é um 
# palíndromo porque permanece "arara" quando lido ao contrário.

# E não palíndromo, por outro lado, é uma sequência que não mantém essa propriedade. Por exemplo, "python" não é um palíndromo 
# porque, quando lido ao contrário, torna-se "nohtyp", que é diferente de "python".
