SELECT cliente.nome, cliente.cpf, ordem.nome, ordem.ticket, ordem.valor_compra, ordem.quantidade_compra ,ordem.data_compra
	FROM cliente, ordem where cliente.id = ordem.cliente_id;
	
	