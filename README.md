# assinarPDFlocal
Código multiplataforma em python para desenho de assinatura em PDFs.
Precisei colocar uma assinatura em cerca de 9 PDFs para um projeto, então criei esse script pra fazer isso automaticamente.

Bibliotecas necessárias:
```
pip install reportlab PyPDF2
```

O comando para uso é bem simples: 

```bash
python assinarpdf.py <arquivo.pdf> <x> <y> [pagina] [largura] [altura]
```


Basta mudar o nome "contrato.pdf" para o local/nome do seu arquivo e trocar os campos pelos respectivos valores. O "x" e "y" onde a assinatura será desenhada é obrigatório, e caso não hajam os argumentos 4, 5 e 6, eles assumirão os valores: 0 (primeira página), largura = 200 e altura = 100 (definido no código). 
É possível com pouco esforço criar um .bat pra executar o script em todos os arquivos de uma pasta, caso queira.
