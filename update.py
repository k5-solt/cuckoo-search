import random
import main
import levy_flight
import fitness

def switch_R(x, y, curr_gen, machines):
    for i in range(main.starting_population_size):
        #移動距離mの取得
        m = levy_flight.m_num(x * y)
        #i番目の解候補をtemp_genにコピー
        temp_gen = curr_gen.solutions[i * x * y : (i + 1) * x * y].copy()
        for j in range(m):
                rand_index = random.randrange(x * y)
                rand_index2 = random.randrange(x * y)
                while(rand_index == rand_index2):
                    rand_index2 = random.randrange(x * y)

                temp = temp_gen[rand_index]

                temp_gen[rand_index] = temp_gen[rand_index2]
                temp_gen[rand_index2] = temp
        #更新前と後のfitnessを比較
        temp_gen_fitness = fitness.prepare_to_judge_specimen(temp_gen.reshape(x,y), machines)
        if curr_gen.population_fitnesses[i]  >=  temp_gen_fitness:
            curr_gen.solutions[i * x * y : (i + 1) * x * y] = temp_gen.copy()  
    return curr_gen
