import pygame
import random
import time

HEIGHT = 600
WIDTH = 1000


class Game:
    def __init__(self, text_length=30):
        self.pool_of_words = ['Master', 'Jane', 'for', 'help', 'quire', 'hear', 'remote',
                              'sister', 'dark', 'remote', 'they', 'was', 'saw', 'shall',
                              'Paris', 'dear', 'ramen', 'pizza', 'when', 'literature',
                              'pineapple', 'good', 'rose', 'tomorrow', 'shield', 'wizard',
                              'people', 'dog', 'cat', 'shepherd', 'kiss', 'dear', 'cally',
                              'animals', 'a', 'if', 'yes', 'no', 'keys', 'mouse', 'beard',
                              'lily', 'the', 'rise', 'python', 'coding', 'beautiful', 'mercy',
                              'gold', 'red']
        self.accuracy = 0
        self.displayed = []
        self.speed = 0
        self.text_length = text_length

    def displaying_words(self):
        # displaying and then storing random words
        for i in range(0, self.text_length):
            self.displayed.append(self.pool_of_words[random.randint(0, 49)])

        return self.displayed

    def calculating_speed(self, user_input, total_time):
        typed = user_input.split()
        length = len(typed)

        # if the player takes this much time to type these many word then how many words in 60 seconds
        self.speed = int(length * (60 / total_time))

        return self.speed

    def calculating_accuracy(self, user_input):
        count = 0
        typed = user_input.split()

        # converting list to string to calculate total number of characters in the displayed sentence
        str = " "
        string = str.join(self.displayed)

        length_displayed = len(self.displayed)
        length = len(typed)

        if length > length_displayed:
            length = length_displayed

        temp = 0  # temporary variable

        # checking every word and if there is an error then finding how many characters did the player get write
        for i in range(0, length):
            if typed[i] == self.displayed[i]:
                count += len(typed[i]) + 1  # counting the blank
            else:
                if len(typed[i]) <= len(self.displayed[i]):
                    temp = len(typed[i])
                else:
                    temp = len(self.displayed[i])

                for j in range(0, temp):
                    if typed[i][j] == self.displayed[i][j]:
                        count += 1

                count += 1  # counting the blank

        # depending on the ratio between number of correct characters and total characters
        self.accuracy = int((count / (len(string) + 1)) * 100)

        return self.accuracy


def display_text(scree, msg, y, fsize, color):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(WIDTH/2, y))
    screen.blit(text, text_rect)
    pygame.display.update()


if __name__ == '__main__':
    # initializing pygame
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Title and icon

    # initializing variables
    player = Game()
    displayed = player.displaying_words()
    text1 = " ".join(displayed[0:10])
    text2 = " ".join(displayed[10:20])
    text3 = " ".join(displayed[20:30])

    # main loop
    running = True
    typing = False
    input_text = ''
    finish = False
    total_time = 1
    speed = 0
    accuracy = 0
    clock = pygame.time.Clock()

    while running:

        screen.fill((0, 0, 0))
        pygame.time.delay(20)
        clock.tick(5)

        # drawing text bar, heading and sample text on the screen
        pygame.draw.rect(screen, (255, 213, 102), (0, 320, 1000, 50), 2) # position of text bar
        display_text(screen, "Typing Speed Game", 100, 64, (255, 213, 102))
        display_text(screen, text1, 220, 25, (255, 255, 255))
        display_text(screen, text2, 250, 25, (255, 255, 255))
        display_text(screen, text3, 280, 25, (255, 255, 255))
        display_text(screen, input_text, 345, 25, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 320 <= y <= 370:
                    typing = True
                    time_start = time.time()
                    input_text = ' '
                elif 480 <= x <= 520 and 480 <= y <= 510:
                    typing = False
                    input_text = ''
                    finish = False
                    total_time = 1
                    speed = 0
                    accuracy = 0

            if event.type == pygame.KEYDOWN:
                if typing and not finish:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        finish = True
                        typing = False
                        end_time = time.time()
                        total_time = end_time - time_start
                    else:
                        input_text += event.unicode
        if finish and not typing:
            speed = player.calculating_speed(input_text, total_time)
            accuracy = player.calculating_accuracy(input_text)
            display_text(screen,"Speed: " + str(speed) + "WPM",  420, 25, (255, 213, 102))
            display_text(screen, "Accuracy: " + str(accuracy)+"%", 455, 25, (255, 213, 102))
            display_text(screen, "Reset", 500, 25, (0, 213, 102))

        pygame.display.update()

