        last_item = exec_query(conn_args=conn_args,
                               sql_query=f'select * from "{settings.DB_SCHEMA}"."commonAttributes" order by id limit 1;')
        if last_item.empty:
            file_id = 0
        else:
            file_id = last_item["file_id"].squeeze()
