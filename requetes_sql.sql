SELECT 
    T.date,
    SUM(T.prod_price*T.prod_qty) AS ventes
FROM TRANSACTION AS T
WHERE T.date BETWEEN "2019-01-01" AND "2019-12-31"
GROUP BY T.date
ORDER BY T.date DESC
;
SELECT 
    T.client_id,
    SUM(
        CASE 
            WHEN P.product_type = "MEUBLE" THEN T.prod_price*T.prod_qty
            ELSE 0
        END
    ) AS ventes_meuble,
    SUM(
        CASE 
            WHEN P.product_type = "DECO" THEN T.prod_price*T.prod_qty
            ELSE 0
        END
    ) AS ventes_deco

FROM TRANSACTION AS T
INNER JOIN PRODUCT_NOMENCLATURE AS P ON P.product_id=T.prod_id
WHERE T.date BETWEEN "2020-01-01" AND "2020-12-31"
GROUP BY T.client_id
