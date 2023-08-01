CREATE TABLE IF NOT EXISTS public.cliente
(
    id SERIAL PRIMARY KEY,
    nome character varying(100) NOT NULL,
    cpf character varying(14) NOT NULL UNIQUE,
    rg character varying(20) NOT NULL,
    data_nascimento date NOT NULL,
    cep character varying(10) NOT NULL,
	logradouro character varying(50) NOT NULL,
	numero character varying(5) NOT NULL,
	complemento character varying(20) NOT NULL,
	bairro character varying(20) NOT NULL,
	cidade character varying(15) NOT NULL,
	uf character varying(2) NOT NULL,
	ddd character varying(6) NOT NULL
);