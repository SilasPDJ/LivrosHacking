import os

exe = os.system


class Routine:
    link_path = 'https://github.com/SilasPDJ/LivrosHacking'
    destiny_url = 'https://github.com/SilasPDJ/LivrosHacking'

    def clone(self):
        exe(f'git clone {self.link_path}')

    def initial(self):
        exe('git init')
        exe('git add . && git status')
        self.fetch()

    def add_origin(self, url=None):
        url = self.destiny_url if url is None else url
        exe(f'git add origin {url}')
        self.fetch()

    def push_commit(self, commit):
        exe(f"git commit -m {commit}")
        self.fetch()
        exe(f'git push -u origin')

    def pull_from(self):
        exe('git pull')

    def fetch(self):
        exe('git fetch')


DALE = Routine()
# DALE.clone()
DALE.initial()
DALE.push_commit('dale')
