# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко; ● D, G – 2 очка; ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка; ● K – 5 очков; ● J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко; ● Д, К, Л, М, П, У – 2 очка; ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка; ● Ж, З, Х, Ц, Ч – 5 очков; ● Ш, Э, Ю – 8 очков; ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
LetterEnglish1 = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'}
LetterEnglish2 = {'D', 'G'}
LetterEnglish3 = {'B', 'C', 'M', 'P'}
LetterEnglish4 = {'F', 'H', 'V', 'W', 'Y'}
LetterEnglish5 = {'K'}
LetterEnglish8 = {'J', 'X'}
LetterEnglish10 = {'Q', 'Z'}
LetterRussian1 = {'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'}
LetterRussian2 = {'Д', 'К', 'Л', 'М', 'П', 'У'}
LetterRussian3 = {'Б', 'Г', 'Ё', 'Ь', 'Я'}
LetterRussian4 = {'Й', 'Ы'}
LetterRussian5 = {'Ж', 'З', 'Х', 'Ц', 'Ч'}
LetterRussian8 = {'Ш', 'Э', 'Ю'}
LetterRussian10 = {'Ф', 'Щ', 'Ъ'}

score = 0
Word = input("Введите слово: ")
WordList = list(Word.upper())
for i in range(len(WordList)):
    if WordList[i] in LetterEnglish1:
        score += 1
    elif WordList[i] in LetterEnglish2:
        score += 2
    elif WordList[i] in LetterEnglish3:
        score += 3
    elif WordList[i] in LetterEnglish4:
        score += 4
    elif WordList[i] in LetterEnglish5:
        score += 5
    elif WordList[i] in LetterEnglish8:
        score += 8
    elif WordList[i] in LetterEnglish10:
        score += 10
    if WordList[i] in LetterRussian1:
        score += 1
    elif WordList[i] in LetterRussian2:
        score += 2
    elif WordList[i] in LetterRussian3:
        score += 3
    elif WordList[i] in LetterRussian4:
        score += 4
    elif WordList[i] in LetterRussian5:
        score += 5
    elif WordList[i] in LetterRussian8:
        score += 8
    elif WordList[i] in LetterRussian10:
        score += 10
print(f'В слове {Word} - {score} очков')