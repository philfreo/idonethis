# Simple iDoneThis CLI script

Because visiting [iDoneThis.com](https://idonethis.com/) and navigating to the right team each day is no fun.

## Install

Install globally:

```sh
git clone https://github.com/philfreo/idonethis
cd idonethis
ln -s $PWD/idonethis.py /usr/local/bin/idonethis
```

## Configure

In your `.bashrc` or `.zshrc`:

```sh
# See https://idonethis.com/api/token/
export IDONETHIS_USERNAME='FILL ME IN'
export IDONETHIS_TOKEN='FILL ME IN'
export IDONETHIS_TEAM='FILL ME IN' # from team page URL
```

## Usage:

### See your dones for the day:

```sh
$ ./idonethis.py
-Caught up on #recruiting tasks
-Pushed some awesome code
-Fix the bugs
```

### Add a done:

```sh
./idonethis.py "Added the coolest feature"
```

## Requirements:

Python, Requests

## License

MIT
