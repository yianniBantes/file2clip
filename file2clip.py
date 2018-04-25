#!/usr/bin/python
import os
import sys
import pyperclip

def main():
  if len(sys.argv) < 2 or any(map(lambda el: el == '--help', sys.argv[1:])):
    print "Usage: ./file2clip.py <file-for-clipboard>"
    sys.exit(0)
  if os.path.exists(sys.argv[1]):
    f = open(str(sys.argv[1]), 'r').read()
    try:
      pyperclip.copy(f)
    except:
      print "File doesn't seem to be a text file, exiting..."
      sys.exit(0)
    print "File copied on clipboard"
  else:
    print "The file doesn't exist! "
    return

if __name__ == "__main__":
    main()
