import sys
msg = sys.stdin.read().replace('feat: ', '').replace('chore: ', '')
sys.stdout.write(msg)
