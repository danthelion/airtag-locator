TODO

1. Redo with Python 3.8 as target postgresql only works with that
2. Start db
3. test EL T
4. add superset
5. visualize

ELT
```shell
TAP_FINDMY_ITEM_NAME='Dániel’s Backpack' \
TARGET_POSTGRES_USER=meltano \
TARGET_POSTGRES_PASSWORD=meltano \
TARGET_POSTGRES_DBNAME=warehouse \
meltano run load-item-location-from-cache
```

BI
```shell
MAPBOX_API_KEY=xxy \
meltano invoke superset:ui
```


setup for post:
1. custom tap to extract data
2. postgresql target
3. dbt to clean up data
4. sqlfluff to clean up models
5. superset to visualize
6. meltano wrap tasks in job
7. meltano orchestrate to run every day
8. airflow validation
