"""Textos das páginas de Privacidade e Termos de Uso (pt-BR e English).

Escritos a partir do que o app e o servidor de licenças realmente fazem. Antes de abrir a loja,
peça a um advogado para revisar e preencha CONTROLLER e CONTACT_EMAIL em build.py.
"""

UPDATED = "8 de novembro de 2026"
UPDATED_EN = "November 8, 2026"

# Cada página: lista de (título da seção, [parágrafos ou listas]). Uma lista vira <ul>.
PRIVACY = {
    "pt": [
        ("Resumo", [
            "O Great COTW One roda no seu computador. Ele lê o save do theHunter: Call of the Wild e a instalação do jogo para mostrar informações e, no Premium, gravar as mudanças que você confirmar. Seu save, seus caminhos de pasta, seu nome de usuário e seu ID da Steam não saem do seu computador.",
            "O app não tem telemetria, não tem análise de uso, não mostra anúncios e não vende dados.",
        ]),
        ("Quem é o responsável", [
            "{controller}, responsável pelo tratamento dos dados descritos aqui (controlador, nos termos da Lei Geral de Proteção de Dados, Lei nº 13.709/2018). Contato e encarregado: {contact}.",
        ]),
        ("O que fica só no seu computador", [[
            "Save do jogo, estatísticas, missões, conquistas e equipamentos lidos do save.",
            "Cópias de segurança feitas antes de cada gravação, na pasta de dados do app.",
            "Ícones lidos do jogo instalado, guardados em cache local.",
            "Preferências: idioma, limite de peso digitado, procurar atualizações ao abrir.",
            "A chave de licença Premium, conferida sem internet.",
        ]]),
        ("Quando o app usa a internet", [
            "Em três situações, e só nelas:",
            [
                "Procurar atualizações: o app lê um arquivo público de versões hospedado no GitHub. Nenhum dado seu é enviado; como em qualquer acesso a um site, o GitHub recebe o endereço IP da sua conexão. Você pode desligar essa procura em Ajustes.",
                "Baixar uma atualização: o instalador novo vem do GitHub e só é instalado se tiver a nossa assinatura digital.",
                "Comprar o Premium: o app envia ao nosso servidor de licenças o plano escolhido e um código aleatório criado no seu computador, para ligar o pagamento à sua chave.",
            ],
        ]),
        ("Dados da compra", [
            "O pagamento é feito na página do Mercado Pago (Pix, cartão e os outros meios que ele oferecer). Nós não recebemos nem guardamos dados de cartão.",
            "Depois que o Mercado Pago confirma o pagamento, nosso servidor guarda: o código aleatório da compra, o identificador do pagamento, o plano, a data, o e-mail do comprador informado ao Mercado Pago e a chave emitida. O e-mail vai escrito dentro da chave, para identificar quem comprou.",
            "Usamos esses dados para entregar e reenviar a licença, dar suporte, tratar reembolsos e cumprir obrigações fiscais e legais.",
        ]),
        ("Bases legais", [[
            "Execução de contrato: entregar o plano comprado e dar suporte.",
            "Cumprimento de obrigação legal: registros fiscais e de consumo.",
            "Legítimo interesse: prevenir fraude e abuso na loja (por exemplo, limitar tentativas por endereço IP), sem guardar o IP depois disso.",
        ]]),
        ("Com quem compartilhamos", [[
            "Mercado Pago: processa o pagamento.",
            "GitHub: hospeda este site, os downloads e o arquivo de versões.",
            "Provedor do servidor de licenças: {host}.",
        ], "Não vendemos nem alugamos dados a ninguém."]),
        ("Por quanto tempo guardamos", [
            "Os dados da compra ficam guardados enquanto a licença for válida e depois pelo prazo exigido pela legislação fiscal e de defesa do consumidor. Passado esse prazo, são apagados.",
        ]),
        ("Seus direitos", [
            "Você pode pedir a confirmação de que tratamos seus dados, acesso, correção, anonimização, portabilidade, eliminação dos dados que não precisamos guardar por lei e informação sobre compartilhamento, escrevendo para {contact}. Respondemos em até 15 dias. Você também pode reclamar à Autoridade Nacional de Proteção de Dados (ANPD).",
        ]),
        ("Segurança", [
            "A licença é assinada com criptografia Ed25519 e conferida sem internet. A conversa com o servidor é só por HTTPS. O servidor confere a assinatura dos avisos do Mercado Pago e consulta o pagamento direto na API antes de emitir qualquer chave. As atualizações só são instaladas com a nossa assinatura.",
        ]),
        ("Crianças e adolescentes", [
            "O app é feito para jogadores do theHunter: Call of the Wild. A compra do Premium deve ser feita por maior de 18 anos ou com o consentimento dos pais ou responsáveis.",
        ]),
        ("Mudanças nesta política", [
            "Se esta política mudar, publicamos a nova versão aqui com a data no fim da página.",
        ]),
    ],
    "en": [
        ("Summary", [
            "Great COTW One runs on your computer. It reads your theHunter: Call of the Wild save and game install to show information and, with Premium, write the changes you confirm. Your save, folder paths, user name and Steam ID never leave your computer.",
            "The app has no telemetry, no usage analytics, no ads, and we do not sell data.",
        ]),
        ("Who is responsible", [
            "{controller} is the data controller under Brazil's General Data Protection Law (LGPD, Law 13,709/2018). Contact and data protection officer: {contact}.",
        ]),
        ("What stays on your computer", [[
            "Your game save, statistics, missions, achievements and equipment read from it.",
            "Backups made before every write, in the app's data folder.",
            "Icons read from your installed game, kept in a local cache.",
            "Preferences: language, the weight limit you type, checking for updates on start.",
            "Your Premium license key, checked offline.",
        ]]),
        ("When the app uses the internet", [
            "Only in three cases:",
            [
                "Checking for updates: the app reads a public versions file hosted on GitHub. None of your data is sent; as with any website, GitHub sees your connection's IP address. You can turn this off in Settings.",
                "Downloading an update: the new installer comes from GitHub and is only installed if it carries our digital signature.",
                "Buying Premium: the app sends our license server the chosen plan and a random code created on your computer, to link the payment to your key.",
            ],
        ]),
        ("Purchase data", [
            "Payment happens on Mercado Pago's page (Pix, card and other methods it offers). We never receive or store card data.",
            "After Mercado Pago confirms the payment, our server stores: the purchase's random code, the payment ID, the plan, the date, the buyer e-mail reported by Mercado Pago and the issued key. The e-mail is written inside the key to identify the buyer.",
            "We use this data to deliver and resend the license, provide support, handle refunds and meet tax and legal obligations.",
        ]),
        ("Legal bases", [[
            "Performance of a contract: delivering the plan and support.",
            "Legal obligation: tax and consumer records.",
            "Legitimate interest: preventing fraud and abuse in the store (for example, limiting attempts per IP address), without keeping the IP afterwards.",
        ]]),
        ("Who we share with", [[
            "Mercado Pago: processes the payment.",
            "GitHub: hosts this website, the downloads and the versions file.",
            "License server provider: {host}.",
        ], "We do not sell or rent data to anyone."]),
        ("How long we keep it", [
            "Purchase data is kept while the license is valid and then for the period required by tax and consumer law, after which it is deleted.",
        ]),
        ("Your rights", [
            "You may ask for confirmation of processing, access, correction, anonymization, portability, deletion of data we are not legally required to keep and information about sharing, by writing to {contact}. We reply within 15 days. You may also complain to Brazil's data protection authority (ANPD).",
        ]),
        ("Security", [
            "Licenses are signed with Ed25519 and checked offline. The app talks to our server over HTTPS only. The server verifies Mercado Pago's webhook signature and checks the payment directly in its API before issuing any key. Updates are only installed with our signature.",
        ]),
        ("Children", [
            "The app is made for theHunter: Call of the Wild players. Premium must be bought by an adult or with the consent of a parent or guardian.",
        ]),
        ("Changes", [
            "If this policy changes, we publish the new version here with the date at the bottom.",
        ]),
    ],
}

TERMS = {
    "pt": [
        ("1. Quem somos", [
            "O Great COTW One é um aplicativo independente de {controller} para o jogo theHunter: Call of the Wild. Não temos ligação com a Expansive Worlds nem com a Avalanche Studios; o nome do jogo é marca dos seus titulares. Ao instalar ou usar o app, você aceita estes termos.",
        ]),
        ("2. Licença de uso", [
            "Damos a você uma licença pessoal, não exclusiva e intransferível para instalar e usar o app nos seus computadores. O app e o seu código são protegidos por direitos autorais. Não é permitido copiar, modificar, descompilar, redistribuir, revender, sublicenciar nem contornar a verificação de licença.",
        ]),
        ("3. Gratuito e Premium", [[
            "Gratuito: tudo o que lê o seu jogo (mapa, animais, perfil, missões, equipamentos, recomendações e backups).",
            "Premium: as funções que gravam no seu save (liberar zonas, editar animais, entregar itens, ajustar munição e dinheiro).",
        ]]),
        ("4. Preço, pagamento e validade", [[
            "Mensal: R$ 15, válido por 31 dias a partir da compra.",
            "Anual: R$ 75, válido por 366 dias a partir da compra.",
            "O pagamento é único e antecipado, pelo Mercado Pago. Não há renovação nem cobrança automática: quando a licença vence, o app volta ao modo gratuito sem apagar nada, e você compra de novo se quiser.",
            "A chave é ativada sozinha no app depois que o Mercado Pago confirma o pagamento, e fica ligada ao e-mail do comprador.",
            "Os preços podem mudar para compras futuras; uma licença já paga vale até o fim do período comprado.",
        ]]),
        ("5. Arrependimento e reembolso", [
            "Pelo Código de Defesa do Consumidor (art. 49), você pode desistir da compra em até 7 dias corridos após o pagamento e receber o valor de volta, sem precisar justificar. Peça pelo {contact} informando o e-mail da compra. Depois do reembolso, a licença deixa de poder ser usada.",
            "Fora desse prazo, avaliamos reembolsos caso a caso quando o Premium não funcionar no seu computador e o suporte não conseguir resolver.",
        ]),
        ("6. Uso permitido", [[
            "Use o app só em partidas single-player. É proibido usá-lo para obter vantagem em modos online, competições ou contra outros jogadores.",
            "A chave Premium é pessoal: não compartilhe, publique nem revenda.",
            "Não use o app para violar os termos do jogo, da Steam ou a lei.",
        ]]),
        ("7. Seu save e os riscos", [
            "Antes de cada gravação o app guarda uma cópia completa, se recusa a gravar com o jogo aberto, mostra o que vai mudar e confere o arquivo depois. Mesmo assim, editar um save é uma escolha sua. Mantenha também as suas cópias. Atualizações do jogo podem mudar o formato dos arquivos; nesse caso, o app pode deixar de ler ou gravar até ser atualizado.",
        ]),
        ("8. Garantia e responsabilidade", [
            "O app é fornecido como está. Fazemos o possível para que funcione bem e corrigimos defeitos nas atualizações, mas não garantimos que funcione sem falhas em todos os computadores ou em todas as versões do jogo. Na medida permitida pela lei, não respondemos por perda de progresso, conquistas, punições aplicadas por terceiros ou outros danos indiretos. Nada aqui limita os seus direitos de consumidor.",
        ]),
        ("9. Atualizações", [
            "O app pode procurar e instalar versões novas, sempre assinadas por nós. Você pode desligar a procura automática em Ajustes. Podemos mudar ou remover funções para acompanhar o jogo; se uma mudança tirar algo essencial do Premium durante a sua licença, você pode pedir reembolso proporcional.",
        ]),
        ("10. Suporte", [
            "Pelo {contact}. Em Ajustes, o botão Copiar relatório para o suporte gera um texto sem dados pessoais que ajuda a resolver o problema.",
        ]),
        ("11. Privacidade", [
            "O tratamento de dados está na Política de Privacidade, que faz parte destes termos.",
        ]),
        ("12. Mudanças e foro", [
            "Podemos atualizar estes termos; a versão vigente fica nesta página com a data no fim. Vale a lei brasileira. Fica eleito o foro do domicílio do consumidor.",
        ]),
    ],
    "en": [
        ("1. Who we are", [
            "Great COTW One is an independent app by {controller} for the game theHunter: Call of the Wild. We are not affiliated with Expansive Worlds or Avalanche Studios; the game's name is a trademark of its owners. By installing or using the app you accept these terms.",
        ]),
        ("2. License", [
            "We grant you a personal, non-exclusive, non-transferable license to install and use the app on your computers. The app and its code are protected by copyright. You may not copy, modify, decompile, redistribute, resell, sublicense or bypass the license check.",
        ]),
        ("3. Free and Premium", [[
            "Free: everything that reads your game (map, animals, profile, missions, equipment, recommendations and backups).",
            "Premium: the features that write to your save (unlocking zones, editing animals, giving items, adjusting ammo and cash).",
        ]]),
        ("4. Price, payment and validity", [[
            "Monthly: R$ 15, valid for 31 days from purchase.",
            "Yearly: R$ 75, valid for 366 days from purchase.",
            "Payment is one-off and upfront, through Mercado Pago. There is no automatic renewal or charge: when the license expires the app returns to free mode without deleting anything, and you buy again if you want.",
            "The key is activated in the app automatically once Mercado Pago confirms the payment, and is tied to the buyer's e-mail.",
            "Prices may change for future purchases; a paid license stays valid until the end of its period.",
        ]]),
        ("5. Withdrawal and refunds", [
            "Under the Brazilian Consumer Code (art. 49) you may cancel within 7 calendar days after payment and get your money back, no questions asked. Ask through {contact} with the purchase e-mail. After a refund, the license may no longer be used.",
            "After that period we consider refunds case by case when Premium does not work on your computer and support cannot fix it.",
        ]),
        ("6. Acceptable use", [[
            "Use the app only in single-player games. It may not be used to gain an advantage in online modes, competitions or against other players.",
            "Your Premium key is personal: do not share, publish or resell it.",
            "Do not use the app to break the game's or Steam's terms or the law.",
        ]]),
        ("7. Your save and risks", [
            "Before every write the app makes a full copy, refuses to write while the game is open, shows what will change and checks the file afterwards. Still, editing a save is your choice. Keep your own copies too. Game updates may change file formats; the app may stop reading or writing until it is updated.",
        ]),
        ("8. Warranty and liability", [
            "The app is provided as is. We do our best for it to work well and fix defects in updates, but we do not guarantee it works flawlessly on every computer or game version. To the extent allowed by law, we are not liable for lost progress, achievements, penalties applied by third parties or other indirect damages. Nothing here limits your consumer rights.",
        ]),
        ("9. Updates", [
            "The app may check for and install new versions, always signed by us. You can turn automatic checks off in Settings. We may change or remove features to keep up with the game; if a change removes something essential from Premium during your license, you may ask for a pro-rata refund.",
        ]),
        ("10. Support", [
            "Through {contact}. In Settings, the Copy report for support button creates a text without personal data that helps us solve the problem.",
        ]),
        ("11. Privacy", [
            "Data processing is described in the Privacy Policy, which is part of these terms.",
        ]),
        ("12. Changes and jurisdiction", [
            "We may update these terms; the current version lives on this page with the date at the bottom. Brazilian law applies, and the consumer's domicile is the chosen venue.",
        ]),
    ],
}
