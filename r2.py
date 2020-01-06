def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def deal(lines):
    allen_count = 0
    allen_sticker = 0
    allen_image = 0
    viki_count = 0
    viki_sticker = 0
    viki_image = 0
    for i in lines:
        s = i.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker += 1
            elif s[2] == '圖片':
                allen_image += 1
            else:
                for m in s[2:]:
                    allen_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker += 1
            elif s[2] == '圖片':
                viki_image += 1
            else:    
                for m in s[2:]:
                    viki_count += len(m)
    print('Allen說了', allen_count, '個字')
    print('Allen說了', allen_sticker, '個貼圖')
    print('Allen說了', allen_image, '張圖片')
    print('Viki說了', viki_count, '個字')
    print('Viki說了', viki_sticker, '個貼圖')
    print('Viki說了', viki_image, '張圖片')

def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('-LINE-Viki.txt')
    deal(lines)
  #  print(lines)
 #   write_file('output.txt', lines)

main()