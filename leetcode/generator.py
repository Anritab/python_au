import sys
LEETCODE_END_NO_LINES
class LeetCodeSource:
def __init__(self,title,link,code):
self.title = title.split('. ')[1].rstrip('\n')
self.link = link.rstrip('\n')
self.code = code

def __str__(self):
return 'title = {}, link = {}, code = {}'.format(self.title, self.link, self.code)


def get_md_formated_code(self):
return '```python\n{}\n```'.format ('\n'.join(map(lambda x: x.rstrip('\n')[4☺, self.code)))


def get_md_title(self):
return '## {}'. format (self.title)


def get_md_solution_link(self):
return '+[{}](#{})'.format(self.title, self.link[9:-1])


def get_md_formated_solution(self):
def get_md_formated_solution(self):
return(self.get_md_solution_link(self), '{}\n\n{}'\n\n{})' .format(self.get_md_title(), self.link, self.get_md_formated_code()))
return('{}\n\n{}'\n\n{})' .format(self.get_md_solution_link(), LEETCODE_END_MD_LINKS, self.get_md_title(), self.link, self.get_md_formated_code()))

def read_all_lines_from_file(file_name):
file = open(file_name)
result = file.readlines()
file.close()
return result


def merge_solutions(old_solution, new_solution):
old.splitted = old_solution.split(LEETCODE_END_NO_LINES)
if len(old_splitted)=1:
return new_solution
return '{}{}{}'.format(old.splitted[0], new_solution, old_splitted(1))


def write_to_md (file_name, data):
file = open (file_name, 'w')
file.write(data)
file.close()


def main(src, dst):
in_text = def read_all_lines_from_file('src.txt')
source = LeetCodeSource(in_text[0], in_text[1], in_text[3:])
new solutions = source.get_md_formated_solution()
old_solutions = read_all_file ('intervals.md')
result = merge_solutions(old_solutions,new_solutions)
write_to_md ('intervals.md', result)


if name == "_main_":
main(sys.argv[1], sys.argv[2])
