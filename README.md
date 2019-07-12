# mapera

Map where your money goes.

# etymology

**map**:
represent (an area) on a map; make a map of

**pera(filipino)**:
money, cash, etc

**mapera(filipino)**:
having a lot of money

**mag-ipon**:
to save, to collect, to put together, to hoard

# prerequisites

* [Python 3.x](https://www.python.org/download/releases/3.0/)
* [pipenv](https://github.com/pypa/pipenv)
* [postgresql](https://www.postgresql.org/)

# running

```bash
$ cd ~/to/the/project/directory

# install the dependencies using pipenv
$ pipenv install

# copy and edit the environment variable files
$ cp .env.template .env
$ cp .envrc.template .envrc

# create super user account
$ pipenv run manage.py createsuperuser

# run and serve
$ pipenv run manage.py runserver 0.0.0.0:8000
```

# contributing

***[Imposter syndrome disclaimer](https://github.com/adriennefriend/imposter-syndrome-disclaimer)***: We want your help. No, really.

There may be a little voice inside your head that is telling you that you're not ready to be an open source contributor; that your skills aren't nearly good enough to contribute. What could you possibly offer a project like this one?

We assure you - the little voice in your head is wrong. If you can write code at all, you can contribute code to open source. Contributing to open source projects is a fantastic way to advance one's coding skills. Writing perfect code isn't the measure of a good developer (that would disqualify all of us!); it's trying to create something, making mistakes, and learning from those mistakes. That's how we all improve, and we are happy to help others learn.

Being an open source contributor doesn't just mean writing code, either. You can help out by writing documentation, tests, or even giving feedback about the project (and yes - that includes giving feedback about the contribution process). Some of these contributions may be the most valuable to the project as a whole, because you're coming to the project with fresh eyes, so you can see the errors and assumptions that seasoned contributors have glossed over.

# license

MIT licensed. Please see the bundled [LICENSE](./LICENSE) file for more details.
