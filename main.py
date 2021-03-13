# import logging
# import multiprocessing
# import time
#
#
# logging.basicConfig(
#     level=logging.DEBUG, format='%(processName)s: %(massage)s'
# )
#
# def worker1(i):
#     logging.debug('start')
#     time.sleep(7)
#     logging.debug('end')
#     return i*2
#
#
# if __name__ == '__main__':
#     with multiprocessing.Pool(3) as p:
#         r = p.imap(worker1, [100, 200])
#         logging.debug('executed')
#         logging.debug([i for i in r])


# import string
#
# import random
#
# from Crypto.Ciper import AES
#
#
# #
#
# key = ''.join(
#     random.choice(string.ascii_letters) for _ in range(AES.block_size))
#
#
#
# iv = ''.join(
#     random string
# )
#
# print(string.ascii_letters)
#
# plaintext = 'dffda'
#
# cipher = AES.new(key, AES.MODE_CBC, iv)
#
#
#
# padding_length = AES.block_size - len(plaintext) % AES.block_size
# plaintext += chr(padding_length) * padding_length
#
# cipher2 = AES.new(key, AES.MODE_CBC, ivc)
# cip1





#
#
# from itertools import permutations
# for i in permutations([1,3,3]):
#     print(i)



# # def all_perms(elements: List[int]) -> List[List[int]]:
# #     first = elements[0:1]
# #     rest = elements[1:]
# #
# #     result = []
# #     if len(elements) <= 1:
# #         return [elements]
# #
# #
# #     for perm in all_perms(elements[1:]):
# #         for i in range(len(elements)):
# #             result.append((perm))
# #
#
#
#
# s = 'test'
#
# print(''.join(reversed(s)))


# def palindrome(strings: str) -> bool:
#     len_strings = len(strings)
#
#     if not len_strings:
#         return False
#     if len_strings <= 1:
#         return True
#
#     start, end = 0, len_strings-1
#     while start < end:
#         if strings[start] != strings[end]:
#             return False
#         start += 1
#         end -= 1
#     return True
#
#
# def find_palindrome(strings: str, left: int, right: int):
#     result = []
#     while 0 <= left and right <= len(strings) - 1:
#         if strings[left] != strings[right]:
#             break
#         result.append(strings[left: right+1])
#         left -= 1
#         right += 1
#     return result
#
#
#
# if __name__ == '__main__':
#     print(find_palindrome('afa', 0,2))
#
#
#
#
#
# if __name__ == '__main__':
#     str = 'aba'
#     print(palindrome(str))


from typing import List


#
# def order_even_first_odd_last_v1(numbers: List) -> None:
#
#     even_first, odd_first = [],[]
#     for num in numbers:
#         if num % 2 == 0:
#
#             even_first.append(num)
#         else:
#             odd_first.append(num)
#     numbers[:] = even_first + odd_first
#
#
# def order_even_first_odd_last_v2(numbers: List[int]) ->None:
#
#     i, j = 0, len(numbers) - 1
#
#     while i < j:
#         if numbers[i] % 2 == 0:
#             i += 1
#         else:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#             j -= 1
#
# if __name__ == '__main__':
#
#
# if __name__ == '__main__':
#     l = [23,2,3,5,5,9,8,5]
#     order_even_first_odd_last_v1(l)
#     print(l)

#
# tmp = [None] * len(chars):
# tmp[index] = chars[i]
#
# return ''.join(tmp)

# def order_change_by_indexes_v2(chars: List[str], indexes: List[int]) -> str:
#     i, len_indexes = 0, len(indexes) - 1
#
#     while i < len_indexes:
#         while i != indexes[i]:
#             index = indexes[i]
#
#             chars[i], chars[index] = chars[index], chars[i]
#             indexes[i], indexes[index] = indexes[index], indexes[i]

#
#
# from typing import List, Generator
#
# def generate_primes_v1(number: int) -> List[int]:
#     primes = []
#     for x in range(2, number + 1):
#         for y in range(2, x):
#             if y % x == 0:
#                 break
#         else:
#             primes.append(x)
#     return primes
#
# def generate_primes_v2(number: int) -> List[int]:
#     primes = []
#     cache = {}
#     i = 0
#     for x in range(2, number+1):
#         i += 1
#         is_prime = cache.get(x)
#         if is_prime is False:
#             continue
#         primes.append(x)
#         cache[x] = True
#         for y in range(x*2, number+1, x):
#             cache[y] = False
#         i += 1
#     print(i)
#     return primes
#
#
#
#
# def generate_primes_v2(number: int) -> Generator[int, None, None]:
#     cache = {}
#     i = 0
#     for x in range(2, number+1):
#         i += 1
#         is_prime = cache.get(x)
#         if is_prime is False:
#             continue
#         yield x
#         cache[x] = True
#         for y in range(x*2, number+1, x):
#             cache[y] = False
#         i += 1
#     print(i)
#
#
# if __name__ == '__main__':
#     import time
#
#     start = time.time()
#     print([i for i in generate_primes_v2(69)])
#     print(time.time() - start)
#


# def is_prime(num: int) -> int:


    # if num <= 1:
    #     return False
    # for i in range(2, num):
    #     if num % i == 0:
    #         return False
    # return True
import math


#
#
# def is_prime(num: int) -> bool:
#     if num <= 1:
#         return False
#     if num ==2:
#         return False
#
#     if num % 2 == 0:
#         return False
#
#
#     for i in range(3, math.floor(math.sqrt(num)+1),2):
#          if num % i == 0:
#              return False
#
#     # i = 2
#     # while i*i <= num:
#     #     if num % i == 0:
#     #         return False
#     #     i += 1
#     # return True
#     return True
#
# if __name__ == '__main__':
#
#     print(is_prime(6))


# # import string
# #
# # def caesar_cipher(text: str, shift: int) -> str:
# #     result = ''
# #     len_alphabet = ord('Z') - ord('A') + 1
# #     for char in text:
# #         # if char.isupper():
# #         #     alphabet = string.ascii_uppercase
# #         # elif char.islower():
# #         #     alphabet = string.ascii_lowercase
# #         # else:
# #         #     result += char
# #         #     continue
# #         # index = alphabet.index(char) + shift
# #         # result += alphabet(index)
# #     if char.isupper():
# #         (ord(char) + shift - ord('A')) % len_alphabet + ord('A')
# #     elif char.islower():
# #         result += chr((ord(chr) + shift - ord('a'))  % len_alphabet + ord('a'))
# #
# #     return result
# #
# # def caesar_cipher_hack(text: str):
# #     len_alphabet = ord('z') - ord('a') + 1
# #     len_alphabet = len(string.ascii_uppercase)
# # if __name__ == '__main__':
# #     e =
# #     caesar_cipher('A', 3)
#
#
#
# # import string
# #
# #
# # ALPHABET = string.ascii_uppercase
# #
# # def generate_key(message: str, keyword: str) -> str:
# #     key = keyword
# #     remain_length = len(message) - len(keyword)
# #     for i in range(remain_length):
# #         key += key[i]
# #
# #     return key
# #
# # def encypt(message: str, key:str) -> str:
# #     result = ''
# #     for i, char in
#
#
# import string
#
# ALPHABET = string.ascii_uppercase
#
# class PlugBoard(object):
#     def __init__(self, map_alphabet):
#         self.alphabet = ALPHABET
#         self.forward_map = {}
#         self.backward_map = {}

#
#
# def hanoi(disk: int, src: str, desk: str, center: str):
#     if desk < 1:
#         return
#
#     hanoi(disk-1, src, center, desk)
#
#
#     print(f'move {disk} from {src} to {dest}')
#     hanoi(disk-1, center, desk, src)
#
# if __name__ == '__main__':
#     hanoi(1, 'B', 'C','A')


#
# from typing import List
#
# def generate_passcal_triangle(depth: int) -> List[List[int]]:
#     data = [[1] * (i + 1) for i  in range(depth)]
#     for line in range(2, depth):
#         for i in range(1, line):
#             data[line][i] = data[line-1][i-1] + data[line-1][i]
#
#     return data
# if __name__ == '__main__':
#     print(generate_passcal_triangle(5))



# import contextlib
# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print('<{}>'.format(name))
#             r = f(content)
#
#
#             print('</{}>'.format(name))
#             return r
#         return _wrapper
#     return _tag
# @tag('h2')
# def f(content):
#     print(content)
# # f = tag(f)
# f('test')


#
#
# import contextlib
#
#
# @contextlib.contextmanager
# def tag(name):
#     print('<{}>'.format(name))
#     yield
#     print('</{}>'.format(name))
#
# # @tag('h2')
# # def f(context):
# #     print(context)
# def f():
#     print('test')
#     with tag('h2'):
#
#         print('test')
#         with tag('h4'):
#             print('tesst')
# f()
#
# import contextlib
#
# class tag(contextlib.ContextDecorator):
#     def __init__(self, name):
#         self.name = name
#         self.start_tag = '<{}>'.format(name)
#         self.end_tag = '<{}>'.format(name)
#
#     def __enter__(self):
#         print(self.start_tag + self.end_tag)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#         print(self.end_tag)
# with tag('h2'):
#     raise Exception('error')
#     print('test')

import contextlib

import os
# try:
#     os.remove('somefile.tmp')
# except FileNotFoundError:
#     pass

# import contextlib
# import os
#
# with contextlib.suppress(FileNotFoundError):
#     os.remove('somefile.tmp')


import contextlib
import logging

import sys


# x = input('Enter:')

# print(x)


# for line in sys.stdin:
#     print(line)

# print('hello')
#
# sys.stdout.write('hello')
#
# logging.error('error')
#
# sys.stderr.write('Error')


# import contextlib
# with open('stdout.log', 'w') as f:
#
#
#     with contextlib.redirect_stdout(f):
#         # print()
#         help(sys.stdout)


# import contextlib
#
# def is_ok_job():
#     try:
#         print('do somethihg')
#         raise Exception('Error')
#         return True
#     except Exception:
#
#         return False
# def cleanup():
#     print('clean up')
# # try:
# #     is_ok = is_ok_job()
# #     print('more task')
# # finally:
# #     if not is_ok:
# #         cleanup()
# #
# with contextlib.ExitStack() as stack:
#     stack.callback(cleanup())
#
#
#     is_ok = is_ok_job()
#     print('more task')
#
#     if is_ok:
#         stack.pop_all()
#
# is_ok = is_ok_job()
# print('more task')


import io
import requests
import zipfile


#
# # with open('/tmp/a.txt', 'w') as f:
# #     f.write('test test')
# #
# # with open('/tmp/a.txt', 'r') as f:
# #     print(f.read())
# #
# #
# # f = io.StringIO()
# # f.write(b'string io test')
# # f.seek(0)
# # print(f.read())
#
#
# url = ('https://www.python.jp/')
#
# f = io.BytesIO()
#
# r = requests.get(url)
# f.write(r.content)
#
# with zipfile.ZipFile(f) as z:
#     with z.open('')

import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}


class DeepChainMap()

# a.update(b)
#
# print(a)
# a.update(c)
#
# print(a)
#
# m = collections.ChainMap(a, b, c)
# print(m)
# print(m.maps)
#
# m.maps.reverse()
#
# m.maps.insert(0, {'c': 'CC'})
# del m.maps[0]
# print(m.maps)
#
# # print(m.maps)
#
# m['b'] = (m.maps)
# # print(m.maps)
#
#
# print(m.maps)
# print(m['c'])