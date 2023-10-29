# Sisteme adaptive şi colaborative

DataSet-ul a fost luat de pe [Kaggle](https://www.kaggle.com/datasets/syedmubarak/netflix-dataset-latest-2021/)
,iar acesta contine o lista cu filme si detalii despre acestea, precum si rating-ul acestora pe diferite platforme.

Deoarece acesta continea destul de multe coloane (29), am ales sa selectez anumite coloane mai importante si de 
datatype-uri diferite (string, set, timestamp, double). De asemenea, am pastrat un set de 500 de inregistrari 
dupa prelucrarea fisierului .xlsx intr-un format favorabil (json).

Am creat 200 users folosind API-ul si am generat interactiuni de tipul Detail Views si Bookmarks intre users 
si items. Interactiunile au fost create generand un fisier in format json cu o lista de interactiuni alcatuite din 
user (ales random din lista), item (de asemenea ales random) si un timestamp. Folosind API-ul de la Recombee, am 
generat o lista de recomandari pentru un user random si rezultatul a fost salvat intr-un fisier denumit
"recommended-user-x.json".


[//]: # (Link-ul catre repo-ul de github: https://github.com/vred29/sadc-lab)
