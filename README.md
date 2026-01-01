# assinarPDFlocal
Código multiplataforma em python para desenho de assinatura em PDFs.
Precisei colocar uma assinatura em cerca de 9 PDFs para um projeto, então criei esse script pra fazer isso automaticamente.

Bibliotecas necessárias:
```
pip install reportlab PyPDF2
```

O comando para uso é bem simples: 
```
python assinarpdf.py contrato.pdf x_da_assinatura y_da_assinatura numero_da_pagina largura_assinatura altura_assinatura
```

Basta mudar o nome "contrato.pdf" para o nome do seu arquivo (no meu caso os arquivos estavam na mesma pasta do script, mas deve funcionar em arquivos em outros diretorios) e trocar os campos pelos respectivos valores. O "x" e "y" onde a assinatura será desenhada é obrigatório, e caso não hajam os argumentos 4, 5 e 6, eles assumirão os valores: 0 (primeira página), largura = 200 e altura = 100. 
É possível com pouco esforço criar um .bat pra executar o script em todos os arquivos de uma pasta, caso queira.
