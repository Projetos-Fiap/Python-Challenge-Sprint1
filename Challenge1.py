opcao = int(input(f'O que você pretende reciclar: \n 1.Cimento, entulho e tijolo \n 2.Azulejo \n 3.Madeira \n 4.Móveis velhos \n 5.Lixo verde \n 6.Papel, papelão \n 7.Vidro \n 8.Alumínio \n O que não é aceito: \n Lixo domiciliar comum, lixo eletrônico, pilha, óleo, material hospitalar ou industrial'))
opcaoZona = int(input(f'Qual zona de SP você está localizado: \n 1.Zona Sul \n 2.Zona Leste \n 3.Centro \n 4.Zona Oeste \n 5.Zona Norte'))

if opcaoZona == 1: 
    print(f'Esses são os EcoPontos localizados na Zona escolhida: \n Santo Dias — Travessa Rosifloras, nº 301 \n Parque Fernanda — Av. Dr. Salvador Rocco, nº 400 (em frente a Rua Antônio Cânon) \n Olinda — Rua Nelson Brissac, s/nº x Av. Padre Adolfo Kolping \n Cidade Saudável — Rua Pitolomeu, s/nº \n Alvarenga — Estrada do Alvarenga, nº 2475 \n Cupecê — Rua Anália Maria de Jesus, n° 130 — Trav. Av. Cupecê \n Santa Cruz — Rua Santa Cruz, nº 1452 (Baixos Viad. Santa Cruz) \n Alceu Maynard de Araújo — Av. Prof. Alceu Maynard de Araújo, nº 330 ao lado da Central de Triagem \n Vicente Rao — Av. Vicente Rao, n° 308 sentido Diadema (Baixos do Viad. Ver José Diniz) \n Água Espraiada — Baixo Viad. Austregésilo de Athayde X Av. Ver. José Diniz \n Mirandópolis — Av. Casemiro da Rocha, nº 1220 — Esq. com Av. José Maria Whitaker \n Beleza — Rua Campo Novo do Sul s/nº \n Jabaquara — Rua Genaro de Carvalho x Rua Jupatis \n Paraisópolis — Rua Itajuni, Vila Andrade/Setor Grutão de Paraisópolis \n Vila Mariana — Rua Mauricio Francisco Klabin, nº37 \n Saioa — Rua Mary Baida Salem, nº01 \n Vila das Mercês — Rua Italva, nº86 \n Giovani Gronchi — Av. Giovani Gronchi, 3413 x Rua José Dias da Costa')

elif opcaoZona == 2:
    print(f'Esses são os EcoPontos localizados na Zona escolhida: \n Viaduto Eng.º Alberto Badra — Av. Aricanduva, nº 200 — Sob Viad. Eng.º Alberto Barra \n Astarte — Rua Astarte X Av. Aricanduva \n Jardim São Nicolau — Rua Agreste de Itabaiana, nº 590 Esq. Rua Eduardo Kyioshi Shimuta \n Jardim São Paulo — Rua Utaro Kanai ao lado do Posto de Saúde \n Nascer do Sol — Rua Nascer do Sol, nº 356 \n Tereza Cristina — Rua Tereza Cristina, nº 10 X Av. do Estado \n Parque Guarani — Rua Manuel Alves da Rocha, nº 584 \n Moreira — Rua João Batista de Godói, nº 1164 \n Imigrantes — Rua Opixe S/Nº x Rua Frederico Hoeme \n Cipoaba — Rua Padre Luís de Siqueira X Av. Rodolfo Pirani \n Iguatemi — Rua Francisco de Melo Palheta x Rua Morro do Frade \n Imperador — Av. Ribeirão Jacu, n° 201 (Baixos do Viad. Jacu Pêssego) \n Carlito Maia — Rua Domingos Fernandes Nobre, nº 109 \n Pedro Nunes — Rua da Polka, nº 100 \n Anhaia Mello — Rua da Prece, nº 296, Altura do nº 2000 da Av. Prof. Luís Ignácio de Anhaia Mello \n São Lucas — Rua Florêncio Sanches, nº 307 Próximo ao 70º Distrito Policial \n Sapopemba — Rua Francesco Usper, nº 550 \n Vila Cardoso Franco — Rua dos Vorás, nº 25 \n Oswaldo Valle Cordeiro — Av. Osvaldo Valle Cordeiro, altura do nº 420 \n Itaqueruna — Rua Domitila D’Abril s/nº x Av. Nordestina \n Nova York — Rua Amélia Vanso Magnoli com as Ruas Olivia Trindade Pinto com Acácio Antunes \n Guaiaponto — Rua da Passagem Funda, 250 \n Mãe Preta — Praça Mãe Preta com a Av. Fernando Figueiredo Lins \n Setor G — Rua Alfonso Asturaro Setor G, altura do nº 600 \n Pesqueiro — Rua Caiuas, nº18 x Avenida Itamerendiba \n Cidade Líder — Rua Francesco Melzi, 200 \n Inácio Monteiro — Rua Regresso Feliz, 1.190, esquina com Rua Cachoeira Morena \n Flamingo — Rua Alexandre Dias Nogueira, 353 \n Tatuapé — Av. Salim Farah Maluf, n°179 (Central de Triagem) \n Penha — Rua Dr. Heládio, nº 104 \n Tiquatira — Rua Amorim Diniz X Av. Gov. Carvalho Pinto s/nº \n Gamelinha — Rua Morfeu, nº 25 X Av. Edgar dos Santos — Jardim Marina \n Vila Matilde — Rua Mateus de Siqueira x Praça Leonildes Ramos Saigo \n Cangaíba — Rua Dr. Luciano Nogueira X Frei Ricardo Pilar \n Franquinho — Rua Carlos Maria Stemberg X Av. Calim Eid \n Belém — Baixos do Via. Guadalajara com Rua Artur Mota x Rua Herval')

elif opcaoZona == 3:
    print(f'Esses são os EcoPontos localizados na Zona escolhida: \n Brás — Rua Palmorino Mônaco x Rua da Moóca (Baixo Viad. Prof. Alberto Mesquita de Carvalho) \n Bresser — Pça. Giuseppe Cesari, n° 54 (Baixos do Viad. Bresser) \n Moóca — Av. Pires do Rio X Rua Bresser (Baixo Viaduto Bresser) \n Glicério — Baixos do Viaduto Glicério \n Liberdade — Rua Jaceguai, Nº 67 x Av. Liberdade \n Armênia — Rua General Carmona, s/nº \n Barra Funda — Rua Sólon (Baixos Viaduto Eng.º Orlando Murgel \n Cambuci — Av. do Estado x Av. D. Pedro I x Rua Ibiruba')

elif opcaoZona == 4:
    print(f'Esses são os EcoPontos localizados na Zona escolhida: \n ')

elif opcaoZona == 5:
    print(f'Esses são os EcoPontos localizados na Zona escolhida: \n ')