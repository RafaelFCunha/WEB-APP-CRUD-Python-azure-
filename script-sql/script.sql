CREATE TABLE [dbo].[Cadastro](
    [id] [int] IDENTITY(1,1) NOT NULL,
    [nome] [varchar](150) NULL,
    [sobrenome] [varchar](150) NULL,
    [email] [varchar](150) NULL,
	[endereco1] [varchar](150) NULL,
	[endereco2] [varchar](150) NULL,	
PRIMARY KEY CLUSTERED 
( [id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]


