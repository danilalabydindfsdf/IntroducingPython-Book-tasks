import unicodedata
import re


def unicode_test(value):
    """The function takes Unicode symbol, finds its name and then
     finds symbol that references to its name(must be the same with the original value"""
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value - {value} name - {name} value2 - {value2}')


def main():
    try:
        unicode_test('E')
    except TypeError as err:
        print(err)

    snowman = '\u2603'
    ds = snowman.encode('utf-8')

    mammoth = """
    We have seen the Queen of cheese,
    Laying quietly at your ease,
    Gently fanned by evening breeze --
    Thy fair form no flies dare seize.

    All gaily dressed soon you'll go
    To the great Provincial Show,
    To be admired by many a beau
    In the city of Toronto.

    Cows numerous as a swarm of bees --
    Or as the leaves upon the trees --
    It did require to make thee please,
    And stand unrivalled Queen of Cheese.
    
    May you not receive a scar as
    We have heard that Mr. Harris
    Intends to send you off as far as
    The great World's show at Paris.
    
    Of the youth -- beware of these --
    For some of them might rudely squeeze
    And bite your cheek; then songs or glees
    We could not sing o' Queen of Cheese.
    
    We'rt thou suspended from baloon,
    You'd cast a shade, even at noon;
    Folks would think it was the moon
    About to fall and crush them soon. 
    """

    # find all worlds that start with 'c'
    pattern = r'\Wc[a-z]*'
    print(f'find all worlds that start with "c": {re.findall(pattern, mammoth)}')

    # find all 4 letters world that starts with 'c'
    pattern = r'\Wc[a-z]{3}\W'
    print(f'find all 4 letters worlds that start with "c": {re.findall(pattern, mammoth)}')

    # find all worlds that end with 'r'
    pattern = r'\W\w*r\W'
    print(f"find all worlds that end with 'r': {re.findall(pattern, mammoth)}")

    # find all worlds that contain 3 vowels letters in a row
    pattern = r'\W\w*[aeiouy]{3}[a-z]'
    print(f"{re.findall(pattern, mammoth)}")


if __name__ == '__main__':
    main()
