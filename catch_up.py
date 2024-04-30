from pygame import *

window = display.set_mode((700,500))
display.set_caption('dogonyalky')
y1 = 10
x1 = 10

y2 = 400
x2 = 400

bg = transform.scale(image.load('background.png'),(700,500))
sp1 = transform.scale(image.load('sprite1.png'),(100,100))
sp2 = transform.scale(image.load('sprite2.png'),(100,100))
game = True
while game:
    k_press = key.get_pressed()
    if k_press[K_UP] and y1 > 0:
        y1 -= 10
    
    if k_press[K_DOWN] and y1 < 410 :
        y1 += 10

    if k_press[K_RIGHT] and x1 < 610:
        x1 += 10

    if k_press[K_LEFT] and x1  > 0 :
        x1 -= 10


    if k_press[K_w] and y2 > 0:
        y2 -= 10
    
    if k_press[K_s] and y2 < 410:
        y2 += 10

    if k_press[K_d] and x2 < 610:
        x2 += 10

    if k_press[K_a] and x2 > 0 :
        x2 -= 10


    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)

    window.blit(bg,(0,0))
    window.blit(sp1,(x1,y1))
    window.blit(sp2,(x2,y2))
    for e in event.get():
        if e.type==QUIT:
            game = False
    display.update()

#создай окно игры

#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»