COPY Warehouse.raw_data FROM '../data/transformed_dataset' WITH DELIMITER AS ';' NULL AS '\null' CSV HEADER;