Тестирование и развертка моделей в производственную среду; конфигурация серверной инфраструктуры; поддержка сервиса для микросервисного приложения "База залогового имущества"
teradatasql.OperationalError: [Version 17.20.0.31] [Session 57461646] [Teradata Database] [Error 2644] SP_MOVE_PRED_TO_CODM:No more room in database PROD_DBML.

SELECT
    DatabaseName,
    SUM(CurrentPerm) AS CurrentPerm,
    SUM(MaxPerm) AS MaxPerm
FROM
    DBC.DiskSpace
WHERE
    DatabaseName = 'PROD_DBML'
GROUP BY
    DatabaseName;