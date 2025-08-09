gokyuzunde_pos = [-0.5065,  0.0998, -0.6540,  0.7317]
bulutlar_pos = [ 0.7295, -0.3170,  1.5783,  1.3409]

dot_product = (
    gokyuzunde_pos[0] * bulutlar_pos[0] +
    gokyuzunde_pos[1] * bulutlar_pos[1] +
    gokyuzunde_pos[2] * bulutlar_pos[2] +
    gokyuzunde_pos[3] * bulutlar_pos[3]
)
print(dot_product) 

cos_sim_uzakligi = gokyuzunde_pos[0] * bulutlar_pos[0]
cos_sim_parlakligi = gokyuzunde_pos[1] * bulutlar_pos[1]
cos_sim_kizilligi = gokyuzunde_pos[2] * bulutlar_pos[2]
cos_sim_maviligi = gokyuzunde_pos[3] * bulutlar_pos[3]

total_cos_sim = cos_sim_uzakligi + cos_sim_parlakligi + cos_sim_kizilligi + cos_sim_maviligi

print(cos_sim_uzakligi, cos_sim_parlakligi, cos_sim_kizilligi, cos_sim_maviligi, total_cos_sim)
