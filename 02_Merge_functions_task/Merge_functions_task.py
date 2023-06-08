from p5 import *
from random import choice, randint

button_images = []  
active_buttons = []  

smile_img = []
light_img = []
circle_image = []
circle_choice_img = ''

num = 60

save_deactive_images = ''
save_button = 'deactive'
frame = True


def setup():
    size(1280, 720)  
    no_stroke()
    load_button_images()

def draw():
    global save_button, frame
    if frame:
        background(255)
        frame = False

    fill("#E6E6E6")
    rect(0, 613, 1280, 108)

    # btn1가 활성화되었을 경우
    if 0 in active_buttons:
        light_choice_img = choice(light_img)
        image(light_choice_img, randint(0, 1280), randint(0, 500))

    #btn3이 활성화 되었을 경우
    if 2 in active_buttons:

        fill(255)
        circle(1280/2, 613/2, 500)

        push_matrix()
        translate(1280 / 2, 613 / 2)  # 캔버스의 중심점을 회전의 중심점으로 설정합니다
        rotate(radians(mouse_x))  # 마우스의 x좌표에 따라 red 이미지를 회전시킵니다.
        image(circle_image[0], -circle_image[0].width/2, -circle_image[0].height/2)

        pop_matrix()

        push_matrix()

        translate(1280 / 2, 613 / 2)  # 캔버스의 중심점을 회전의 중심점으로 설정합니다
        rotate(radians(mouse_y))  # 마우스의 y좌표에 따라 blue 이미지를 회전시킵니다.
        image(circle_image[1], -circle_image[1].width/2, -circle_image[1].height/2)
        pop_matrix()


    #지우개 버튼
    if 5 in active_buttons: 
        frame = True
        active_buttons.remove(5)

    draw_button()


def draw_button():
    global save_button

    #일반 버튼 status
    for i in range(len(button_images)):
        if i in active_buttons:
            active_image = load_image(f"source/btn/btn{i+1}-active.png")
            image(active_image, 355+(i*99), 627, 75, 75)  
        else:
            image(button_images[i], 355+(i*99), 627, 75, 75)  
            

    #save 버튼 status
    if save_button == 'deactive':
        image(save_deactive_images, 1175, 628, 75, 75)
    else:
        save_active_image = load_image("source/btn/save-active.png")
        image(save_active_image, 1175, 628, 75, 75)

def load_button_images():
    global save_deactive_images
    save_deactive_images = load_image('source/btn/save-deactive.png')
    

    #btn1 - red image
    for i in range(4):
        light_img.append(load_image(f'source/btn1_light/light-red-{100 + (i*50)}.png'))

    #btn1 - yellow image
    for i in range(4):
        light_img.append(load_image(f'source/btn1_light/light-yellow-{100 + (i*50)}.png'))

    #btn1 - blue image
    for i in range(4):
        light_img.append(load_image(f'source/btn1_light/light-blue-{100 + (i*50)}.png'))

    #btn2 - smile image
    for i in range(4):
        smile_img.append(load_image(f'source/btn2_smile/smile{50*(i+1)}.png'))

    for i in range(6):
        button_image = load_image(f"source/btn/btn{i+1}-deactive.png")
        button_images.append(button_image)

    #btn3 - circle
    for i in ['blue', 'red', 'yellow']:
        circle_image.append(load_image(f"source/btn3_circle/circle-{i}.png"))



def mouse_pressed():
    global save_button
    global circle_choice_img


    #일반 버튼들 상태 전환
    for i in range(len(button_images)):
        button_x = 355 + (i * 99)
        button_y = 613
        button_width = 75
        button_height = 75

        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
            if i in active_buttons:
                active_buttons.remove(i)
            else:
                active_buttons.append(i)

    save_btn_x = 1175
    save_btn_y = 628

    #save 버튼 상태 전환
    if save_btn_x <= mouse_x <= save_btn_x + button_width and save_btn_y <= mouse_y <= save_btn_y + button_height:
        if save_button == 'deactive':
            save_button = 'active'
        else:
            save_button = 'deactive'

    if 1 in active_buttons: 
        mousey = min(600, mouse_y)  # 마우스의 y 좌표가 613 이상이면 613으로 고정

        choice_smile_img = choice(smile_img)  # 50에서 200 사이의 랜덤 크기 스마일 이미지 선택 
        image(choice_smile_img, mouse_x, mousey)  # width와 height를 랜덤 크기로 설정

run()