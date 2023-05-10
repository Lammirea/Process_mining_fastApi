# Process_mining_fastApi
Данное приложение позволяет построить по журналу событий модель с помощью Alpha, Heuristics и Inductive miner для дальнешего анализа в Process miner.
Также есть возможность выполнить conformance checking с помощью token-based replay на основании inductive miner.

## Правила испозования
<sub>Часть первая</sub>                      
https://github.com/Lammirea/Process_mining_fastApi/assets/71898618/c2569250-9ad3-4d65-9d0f-326a065d02c7

<sub>Часть вторая</sub>
https://github.com/Lammirea/Process_mining_fastApi/assets/71898618/a03eb967-ab40-4b7c-83ed-83868ca013ff

## Назначения папок
1. В папке templates находится файл main.html, в котором реализована вся html часть приложения
2. В static находится файл с css
3. В app находятся файлы с реализациями функций pm4py (minersFunc.py) и FastApi (main.py)
4. Также создана пустая папка buffer для временного хранения журналов событий (после выполнения функций файлы удаляются).
