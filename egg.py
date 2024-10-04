import random
import main
import levy_flight
import fitness


egg_count = 0

def switch(machines, x, y, curr_gen, egg_rate):
    flag = 0
    for i in range(main.starting_population_size):
        #i番目の解候補をtemp_genにコピー
        temp_gen = curr_gen.solutions[i * x * y : (i + 1) * x * y].copy()
        temp_gen_fitness = fitness.prepare_to_judge_specimen(temp_gen.reshape(x,y), machines)
        #print(temp_gen_fitness)

        rand = random.random() 
        if curr_gen.best() == temp_gen_fitness and flag == 0:
            flag = 1
        elif rand < egg_rate:  #egg_rate = 0.001
            #移動距離mの取得
            m = levy_flight.m_num(x * y)
            for j in range(m):
                rand_index = random.randrange(x * y)
                rand_index2 = random.randrange(x * y)
                while(rand_index == rand_index2):
                    rand_index2 = random.randrange(x * y)

                temp = curr_gen.solutions[i * x * y + rand_index]

                curr_gen.solutions[i * x * y + rand_index] = curr_gen.solutions[i*x * y + rand_index2]
                curr_gen.solutions[i * x * y + rand_index2] = temp
            
            global egg_count
            egg_count += 1
    return curr_gen

