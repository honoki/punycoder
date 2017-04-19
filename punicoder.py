# coding=utf-8

import sys
import os
import idna

class punicoder(object):

  homoglyphs = {

    'a': ['а', 'Ꭺ'],
    'b': [],
    'c': ['ϲ','с'],
    'd': ['ԁ'],
    'e': ['е'],
    'f': [],
    'g': ['ɡ'],
    'h': ['һ'],
    'i': ['Ꭵ','і'],
    'j': ['ј','ϳ'],
    'k': [],
    'l': ['ⅼ','ӏ'],
    'm': ['ⅿ'],
    'n': [],
    'o': ['о','ο'],
    'p': ['р'],
    'q': [],
    'r': [],
    's': ['ѕ'],
    't': [],
    'u': ['υ'],
    'v': ['ⅴ','ѵ','ν'],
    'w': ['ѡ'],
    'x': ['х'],
    'y': ['у','γ'],
    'z': []

  }

  '''
  Execute the program.
  '''
  def execute(self, domain_name):

    idns = []
    oldidns = []

    # Walk through all characters in the domain name
    domain = domain_name.rsplit('.', 1)[0]

    # Initially, replace single instances of homoglyphs
    idns = idns + self.replace_homoglyphs([domain])

    # Now iterate over this list again, to replace additional homoglyphs and always remove duplicates
    while not set(oldidns) == set(idns):
      oldidns = idns
      idns = list(set(idns + self.replace_homoglyphs(idns)))

    domains = []
    for idn in idns:
      try:
        clear = (idn + '.' + domain_name.rsplit('.', 1)[1]).encode('utf-8')
        puni = idna.encode(clear.decode('utf-8'))
        print clear, puni
        domains.append(puni)
      except:
        pass
       #print 'INVALID:', clear

  def replace_homoglyphs(self, list):
    replaced = []

    # For every element in the list, replace a character that has a homoglyph
    for domain in list:
      for i in range(0,len(domain)):
        for character in self.homoglyphs:
          if domain[i] == character:
            for glyph in self.homoglyphs[character]:
              domaincopy = u''
              domaincopy = (domain[:i] + glyph.decode('utf-8') + domain[i+1:])
              #print domaincopy
              replaced.append(domaincopy)

    return replaced

if __name__=='__main__':

  if len(sys.argv) < 2 or not '.' in sys.argv[1]:
    print 'Please provide a valid domain name.'
  else:
    domain = sys.argv[1]
    program = punicoder()
    program.execute(domain)
