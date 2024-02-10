SELECT JSONB_BUILD_OBJECT("types"."chave_db",

										JSONB_OBJECT("types".JK,

											"types".JV)) AS "postgres"
		FROM
			(SELECT "type"."chave_db", ARRAY["type"."tipo_db",
					"type"."tipo_python"] AS JK, ARRAY["type"."chave_db",
					"type"."chave_python"] AS JV
				FROM
					(SELECT 'db_type' AS "tipo_db",
							DB_TYPES.DB_TYPE AS "chave_db",
							'python_type' AS "tipo_python",
							'' AS "chave_python"
						FROM DB_TYPES) AS "type") AS "types"