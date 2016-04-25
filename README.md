# Check-Dupes

check-dupe.py: Procura no diretório escolhido por arquivos que possuam
hash sum MD5 iguais fazendo uma lista dos arquivos duplicados.
Argumentos de linha de comando:
    1) Pasta onde procurar: -v para Videos; -p para Pictures;
    2) Subpasta a ser considerada.
    
    Ex.: ./check-dupe -p "2010/Dec" --> Pega arquivos da pasta ~/Pictures/2010/Dec e
procura por duplicatas.
