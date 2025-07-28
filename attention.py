gokyuzunde_pos = [-0.5065,  0.0998, -0.6540,  0.7317]
bulutlar_pos = [ 0.7295, -0.3170,  1.5783,  1.3409]

sertlik_uzaklığı = abs(gokyuzunde_pos[0] - bulutlar_pos[0])
parlaklık_uzaklığı = abs(gokyuzunde_pos[1] - bulutlar_pos[1])
kızıllık_uzaklığı = abs(gokyuzunde_pos[2] - bulutlar_pos[2])
mavilik_uzaklığı = abs(gokyuzunde_pos[3] - bulutlar_pos[3])

print(sertlik_uzaklığı,parlaklık_uzaklığı,kızıllık_uzaklığı,mavilik_uzaklığı)
toplam_uzaklık = sertlik_uzaklığı + parlaklık_uzaklığı + kızıllık_uzaklığı + mavilik_uzaklığı
print(toplam_uzaklık)