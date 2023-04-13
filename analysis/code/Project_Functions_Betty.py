def method_chaining (data):
    
    method_chain_data = (data.dtypes
                        .apply(lambda x: check_delim(data))
                        .apply(lambda x: ~data['EDUCATION'].isin([0, 5, 6]))
                        .apply(lambda x: ~data['MARRIAGE'].isin([0]))
                    )
    return data