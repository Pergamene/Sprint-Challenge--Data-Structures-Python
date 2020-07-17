'''
Print out each element of the following array on a separate line, but this time the input array can contain arrays nested to an arbitrarily deep level:

['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

For the above input, the expected output is:

Bob
Slack
reddit
89
101
alacritty
(brackets)
5
375
0
{slice, owned}
22

You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
'''
data_list = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

def print_list(list_to_print):
  for item in list_to_print:
    if isinstance(item, list):
      print_list(item)
    else:
      print(item)

print_list(data_list)
