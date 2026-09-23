import random

while True:
    print("   DESAFIO DO GINÁSIO POKÉMON - INÍCIO")

    # Configuração inicial dos personagens
    hp_pokemon = 100
    hp_lider = 100
    pontos_treino = 0

    # Usando loop for de 5 iterações para o treinar o pokémon
    print("\n--- FASE 1: TREINAMENTO ---")
    print("Você se prepara para o desafio treinando duro!\n")

    for i in range(1, 6):
        pontos_ganhos = random.randint(5, 10)
        pontos_treino += pontos_ganhos
        
        print(f"Treino {i}/5: Você ganhou {pontos_ganhos} pontos de treino!")

    bonus_dano = pontos_treino // 10

    print(f"\nTreino concluído!")
    print(f"Total de pontos acumulados: {pontos_treino}")
    print(f"Bônus de ataque obtido: +{bonus_dano} de dano extra em cada ataque!")


    # Batalha com while
    print("\n--- FASE 2: BATALHA CONTRA O LÍDER ---")
    turno = 1

    while hp_pokemon > 0 and hp_lider > 0:
        print(f"\n--- TURNO {turno} ---")

        # Ataque do jogador
        meu_dano_base = random.randint(8, 15)
        meu_dano_total = meu_dano_base + bonus_dano
        hp_lider -= meu_dano_total 

        print(f"Seu Pokémon atacou! Causou {meu_dano_total} de dano (Base: {meu_dano_base} + Bônus: {bonus_dano}).")
        print(f"HP do Líder restante: {max(0, hp_lider)}")

        # Verifica a vida do líder
        if hp_lider <= 0:
            print("\nPARABÉNS! Você derrotou o líder do ginásio!")
            break   # Encerra o while

        # Ataque do líder
        dano_lider = random.randint(5, 12)
        hp_pokemon -= dano_lider 

        print(f"O Líder de Ginásio atacou! Causou {dano_lider} de dano.")
        print(f"Seu HP restante: {max(0, hp_pokemon)}")

        # Verifica a vida do jogador
        if hp_pokemon <= 0:
            print("\nVocê perdeu a batalha contra o Líder!")
            break  # Encerra o while

        turno += 1  # Avança para o próximo turno

    # Pergunta se deseja tentar de novo
    opcao = input("Deseja tentar o desafio do Ginásio novamente? (s/n): ").strip().lower()

    if opcao != 's':
        print("\nObrigado por jogar! Até a sua próxima jornada!")
        break