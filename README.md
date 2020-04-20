# Pycrypt

Программа для шифрования, расшифровки и взлома шифра. 
Поддерживаются: 
- шифр Цезаря (шифрование, расшифровка, взлом)
- шифр Виженера (шифрование, расшифровка)
- шифр Вернама (шифрование, расшифрока)

## Запуск:
#### Шифрование и расшифровка:
```
python pycrypt.py {mode} --input_file {input_file} --output_file {output_file} --cypher {cypher} --key {key}
```

_mode_ -- режим работы:
- _encode_ - шифрование
- _decode_ - расшифровка

_cypher_  -- алгоритм шифрования:
- _caesar_ -- шифр Цезаря
- _vigenere_ -- шифр Виженера
- _vernam_ -- шифр Вернама

_input_file_ -- файл исходного текста, если его не указать, то будет консольный ввод.

_output_file_ -- файл, куда записать текст. Если его не указать, то будет консольный вывод. 

_key_ -- ключ шифрования

#### Обучение:

Если вы хотите обучить программу на своём тексте, то введите:
```
python pycrypt.py learn --mode {letters/words} --pack {eng/rus} --input_file {input_file} --output_file {output_file}
```
_mode_ -- режим работы
- _letters_ -- подсчёт частот букв
- _words_ -- нахождение самых частых слов

__Замечание__: никогда не записывайте в один файл результаты работы для разных режимов. 
Т. е. в  одном файле могут находиться результаты либо только _letters_, либо только _words_.
Но в одном файле могут быть результаты для _eng_ и _rus_. 

#### Взлом:
```
python pycrypt.py hack --input_file {input_file} --output_file {output_file} --cypher {cypher} --proba {proba} --words {words}
```
_proba_ -- файл с частотами букв, обязательный аргумент

_words_ -- файл с наиболее употребляемыми словами, необязательный аргумент

Пока доступен взлом только шифра Цезаря. Реализован взлом подсчётом частот букв (для текстов с не менее 5000 символов), 
для меньших текстов происходит подсчёт совпадений слов со словарём наиболее употребряемых слов (если в аргументах указали данный файл)

#### Тесты:
Для запуска тестов введите:
```
python pycrypt.py test
```
